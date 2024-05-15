from pymodbus.client import AsyncModbusTcpClient, ModbusBaseClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder

from config import net_data


class ModbusService:
    client: ModbusBaseClient = AsyncModbusTcpClient(host=net_data.remotehost, port=net_data.remoteport)
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)

    @classmethod
    async def write_float(cls, register, value):
        cls.builder.add_32bit_float(value)
        payload = cls.builder.build()
        await cls.client.write_registers(address=register, values=payload, slave=16, skip_encode=True)

    @classmethod
    def convert_to_float(cls, registers: list):
        decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
        result = decoder.decode_32bit_float()
        return result
