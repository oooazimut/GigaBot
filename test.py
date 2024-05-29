from db.repo import PumpWorkService
from db.repo import GasSensorService
from service.plot import PlotService

data1 = GasSensorService.get_pumps_last_values()
data1 = [i['value'] for i in data1]
data1 = [round(val, 2) for val in data1]
data1.reverse()
print (data1)

PlotService.plot_current_pump(data1, 'g_pump_room')
