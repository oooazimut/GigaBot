from db.repo import PumpWorkService
from db.repo import PressureService
from service.plot import PlotService

data1 = PressureService.get_last_values()
data1 = [i['value'] for i in data1]
data1 = [round(val, 2) for val in data1]
data1.reverse()
data2 = PumpWorkService.get_current()
data2 = [round(int(val) / 3600, 1) for val in data2]

PlotService.plot_current_pump(data1, 'pressures')
PlotService.plot_current_pump(data2, 'pumpworks')
