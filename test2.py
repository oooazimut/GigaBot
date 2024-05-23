from db.repo import PressureService
from service.plot import PlotService

data = PressureService.get_last_values()
if data:
    pressures = [round(i['value'], 1) for i in data]
    p3 = pressures.pop()
    pressures.insert(2, p3)
    PlotService.plot_current_pressures(pressures)
