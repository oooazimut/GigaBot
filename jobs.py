import datetime

from config import _logger, gas_rooms, pumps_ids
from db.repo import Service
from service.functions import chunks, convert_to_bin
from service.modbus import ModbusService


async def save_data():
    data = await ModbusService.polling(16384, 31)
    if data:
        dttm = datetime.datetime.now().replace(microsecond=0)

        temp = data[:12]
        gas_sensors = dict(zip(gas_rooms, (temp[:8], temp[8::])))
        for key in gas_sensors:
            sensors = chunks(gas_sensors[key], 2)
            counter = 0
            for sensor in sensors:
                counter += 1
                value = ModbusService.convert_to_float(sensor)
                Service.save_to_table('gas_levels', [f'{key}.{counter}', value, dttm])

        pressures = dict(zip(pumps_ids, chunks(data[12:22], 2)))
        for pump in pressures:
            value = ModbusService.convert_to_float(pressures[pump])
            Service.save_to_table('pressures', [pump, value, dttm])

        with open('vars.txt', 'w') as fi:
            print(*data[22:27], file=fi)

        if data[28]:
            tanks = dict(enumerate(convert_to_bin(data[28], 3), start=1))
            for tank in tanks:
                if int(tanks[tank]):
                    Service.save_to_table('tank_levels', [str(tank), int(tanks[tank]), dttm])

        if data[29]:
            bypasses = dict(zip(pumps_ids[:-1], convert_to_bin(data[29], 4)))
            for pump in bypasses:
                if int(bypasses[pump]):
                    Service.save_to_table('bypasses', [pump, int(bypasses[pump]), dttm])

        if data[30]:
            sirens = dict(zip(pumps_ids, convert_to_bin(data[30], 5)))
            for pump in sirens:
                if int(sirens[pump]):
                    _logger.warning(f'### работает сирена насоса {pump}')


async def save_pumpwork():
    with open('vars.txt', 'r') as fo:
        data = fo.read()
        if data:
            data = data.split()
            dttm = datetime.datetime.now().replace(microsecond=0)
            pumpworks = dict(zip(pumps_ids, data))
            for pump in pumpworks:
                Service.save_to_table('pumpwork', [pump, int(pumpworks[pump]), dttm])
