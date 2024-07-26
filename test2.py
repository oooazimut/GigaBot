from service.functions import chunks
from service.modbus import ModbusService


some = zip((1, 2), chunks([1, 2, 3, 4,], 2))
print(some, type(some))
for i in some:
    print(i)

