import datetime

import config
import vars
from db.repo import Service
from service.functions import chunks, convert_to_bin, send_message
from service.modbus import ModbusService


async def save_data():
    data = await ModbusService.polling(16384, 41)
    if data:
        dttm = datetime.datetime.now().replace(microsecond=0)

        # Датчики газа
        keys = config.GAS_SENS_DESCS + config.GAS_SENS_PROB_DESCS
        values = map(ModbusService.convert_to_float, chunks(data[:12], 2))
        gas_sensors = (
            "gas_levels",
            [(key, value, dttm) for key, value in zip(keys, values)],
        )

        # Давление насосов
        pressures = (
            "pressures",
            [
                (key, value, dttm)
                for key, value in zip(
                    config.PUMPS_IDS,
                    map(ModbusService.convert_to_float, chunks(data[12:22], 2)),
                )
            ],
        )

        # Наработка насосов
        with open("pumpwork.txt", "w") as fi:
            print(*data[22:27], file=fi)

        # Дренажные ёмкости
        tanks = dict(enumerate(convert_to_bin(data[28], 3), start=1))
        triggered_tanks = list()
        if data[28]:
            for tank in tanks:
                if tanks[tank]:
                    triggered_tanks.append((tank, tanks[tank], dttm))
                    if tanks.get(tank) != vars.levels.get(tank):
                        await send_message(text=f"Переполнение емкости {tank}!")
        vars.levels = tanks
        tanks = ("tank_levels", tanks)

        #  Работа насосов в обход
        bypasses = dict(zip(config.PUMPS_IDS[:-1], convert_to_bin(data[29], 4)))
        triggered_bypasses = list()
        if data[29]:
            for pump in bypasses:
                if bypasses[pump]:
                    triggered_bypasses.append((pump, bypasses[pump], dttm))
                    if bypasses.get(pump) != vars.cheats.get(pump):
                        await send_message(text=f"Насос {pump} работает в обход УЗА!")
        vars.cheats = bypasses
        bypasses = ("bypasses", bypasses)

        # Сработка сирен
        if data[30]:
            sirens = dict(zip(config.PUMPS_IDS, convert_to_bin(data[30], 5)))
            for pump in sirens:
                if int(sirens[pump]):
                    config._logger.warning(f"### работает сирена насоса {pump}")
                    if sirens.get(pump) != vars.sirens.get(pump):
                        await send_message(
                            text=f"отвал уза насоса {pump} во время работы!"
                        )
            vars.sirens = sirens

        Service.save_to_tables(
            [gas_sensors, pressures, triggered_tanks, triggered_bypasses]
        )

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
            pumpworks = dict(zip(config.PUMPS_IDS, data))
            for pump in pumpworks:
                Service.save_to_table("pumpwork", [pump, int(pumpworks[pump]), dttm])


async def morning_mailing():
    text = "Утренняя сводка:\n\n"

    text += "Уровни:\n"
    conditions = {0: "норма", 1: "полная!"}
    for tank in vars.levels:
        text += f"Ёмкость {tank}: {conditions.get(vars.levels[tank])}\n"

    await send_message(text=text)
