from pymodbus import ModbusException, ExceptionResponse

from service.modbus import ModbusService

from config import _logger


async def polling():
    await ModbusService.client.connect()
    assert ModbusService.client.connected, 'Нет соединения с ПР-103'
    try:
        data = await ModbusService.client.read_holding_registers(16384, 31)
        gas_levels = data.registers[:12]
        pressures = data.registers[12:22]
        pumpworks = data.registers[22:27]
        tanklevels = data.registers[28]
        bypasses = data.registers[29]
        sirens = data.registers[30]
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
