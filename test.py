# import asyncio
from service.modbus import ModbusService


async def write_setpoint(register, value):
    await ModbusService.client.connect()
    print(ModbusService.client.connected)
    await ModbusService.client.write_register(register, value)
    ModbusService.client.close()

# asyncio.run(write_setpoint(16429, 5425))
