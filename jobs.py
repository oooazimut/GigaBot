import datetime

from pymodbus import ModbusException, ExceptionResponse

from db.repo import Service
from service.functions import chunks, convert_to_bin
from service.modbus import ModbusService

from config import _logger, gas_rooms, pumps_ids


async def polling(address, count):
    await ModbusService.client.connect()
    assert ModbusService.client.connected, 'Нет соединения с ПР-103'
    try:
        data = await ModbusService.client.read_holding_registers(address, count)
    except ModbusException as exc:
        _logger.error(f'1 {exc}')
        ModbusService.client.close()
        return
    if data.isError():
        _logger.error(data)
        ModbusService.client.close()
        return
    if isinstance(data, ExceptionResponse):
        _logger.error(f' 2 {data}')
        ModbusService.client.close()
        return
    ModbusService.client.close()
    return data.registers


async def save_data():
    data = await polling(16384, 31)
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
