from config import PUMPS_IDS, PUMPS_DESCS
from db.repo import PressureService

data = PressureService.get_last_values()
print(type(data))
[print(i) for i in data]

pumps = list(zip(PUMPS_IDS, PUMPS_DESCS))
print(pumps)
