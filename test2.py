import datetime

from db.repo import PressureService
from service.functions import sort_pressures_by_pumps
from service.plot import PlotService
from config import PUMPS_IDS

data = PressureService.get_last_values()
if data:
    pressures = [round(i['value'], 1) for i in data]
    p3 = pressures.pop()
    pressures.insert(2, p3)
    PlotService.plot_current_pressures(pressures)



date = datetime.date.today() - datetime.timedelta(days=3)
by_date = PressureService.get_values_by_date(date )

# for i in by_date:
#     print(i)
# print(type(by_date))

sorted_data = sort_pressures_by_pumps(by_date)
PlotService.plot_pressures_by_date(sorted_data)
