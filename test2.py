import vars
from config import PUMPS_IDS
from service.functions import convert_to_bin
from service.plot import PlotService


data = map(int, convert_to_bin(vars.pumps, 5))
data = list(zip(PUMPS_IDS, data))
print(data)
data1 = [0, 0, 1, 0, 1, 1]
data3 = list(enumerate(data1, start=1))
data1 = list(zip(PUMPS_IDS, data1))
print(data3)
PlotService.plot_uza({'Data': data, 'Data1': data1, 'SomeShit': data3})
