import asyncio
from service.modbus import ModbusService


client = ModbusService.client

async def write_register():
    await client.connect()
    if client.connected:
        await client.write_register()
        client.close()

# if __name__ == "__main__":
#     asyncio.run(write_register())
