from config import pumps_ids
from service.functions import convert_to_bin

a = convert_to_bin(16, 5)
b = dict(zip(pumps_ids, a))
print(b)
print(a, type(a))