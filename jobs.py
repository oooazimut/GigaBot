import datetime

import vars
from config import GAS_ROOMS, PUMPS_IDS, _logger
from db.repo import Service
from service.functions import chunks, convert_to_bin, send_message
from service.modbus import ModbusService


async def save_data():
    data = await ModbusService.polling(16384, 41)
    if data:
        dttm = datetime.datetime.now().replace(microsecond=0)

        temp = data[:12]
        gas_sensors = dict(zip(GAS_ROOMS, (temp[:8], temp[8::])))
        for key in gas_sensors:
            sensors = chunks(gas_sensors[key], 2)
            counter = 0
            for sensor in sensors:
                counter += 1
                value = ModbusService.convert_to_float(sensor)
                Service.save_to_table("gas_levels", [f"{key}.{counter}", value, dttm])

        pressures = dict(zip(PUMPS_IDS, chunks(data[12:22], 2)))
        for pump in pressures:
            value = ModbusService.convert_to_float(pressures[pump])
            Service.save_to_table("pressures", [pump, value, dttm])

        with open("pumpwork.txt", "w") as fi:
            print(*data[22:27], file=fi)

        if data[28]:
            tanks = dict(enumerate(convert_to_bin(data[28], 3), start=1))
            for tank in tanks:
                if int(tanks[tank]):
                    Service.save_to_table(
                        "tank_levels", [str(tank), int(tanks[tank]), dttm]
                    )
                    if tanks.get(tank) != vars.levels.get(tank):
                        await send_message(text=f"Переполнение емкости {tank}!")
            vars.levels = tanks

        if data[29]:
            bypasses = dict(zip(PUMPS_IDS[:-1], convert_to_bin(data[29], 4)))
            for pump in bypasses:
                if int(bypasses[pump]):
                    Service.save_to_table("bypasses", [pump, int(bypasses[pump]), dttm])

        if data[30]:
            sirens = dict(zip(PUMPS_IDS, convert_to_bin(data[30], 5)))
            for pump in sirens:
                if int(sirens[pump]):
                    _logger.warning(f"### работает сирена насоса {pump}")
                    if sirens.get(pump) != vars.sirens.get(pump):
                        await send_message(
                            text=f"отвал уза насоса {pump} во время работы!"
                        )
            vars.sirens = sirens

        vars.uzas = data[32]
        vars.permissions = data[33]
        vars.pumps = data[34]
        vars.shifters = data[35::]


async def save_pumpwork():
    with open("pumpwork.txt", "r") as fo:
        data = fo.read()
        if data:
            data = data.split()
            dttm = datetime.datetime.now().replace(microsecond=0)
            pumpworks = dict(zip(PUMPS_IDS, data))
            for pump in pumpworks:
                Service.save_to_table("pumpwork", [pump, int(pumpworks[pump]), dttm])


async def morning_mailing():
    text = "Утренняя сводка:\n\n"

    text += "Уровни:\n"
    conditions = {"0": "норма", "1": "полная!"}
    for tank in vars.levels:
        text += f"Ёмкость {tank}: {conditions.get(vars.levels[tank])}\n"

    await send_message(text=text)
