from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(
    host='kitvideovpn.ru',
    port=8454
)

client.connect()
print(client.connected)
responce = client.read_holding_registers(16406, 5)
print(responce.registers)
client.close()