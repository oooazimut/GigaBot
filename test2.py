import vars
from config import PUMPS_IDS
from service.functions import convert_to_bin


l = [1, 1, 2, 5]
l.append(l[-1])
res = list(zip(PUMPS_IDS, l))
print(res)
l.insert(0, 0)
print(l)
