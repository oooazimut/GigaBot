from db.repo import PumpWorkService, GasSensorService
from db.repo import PressureService
from service.plot import PlotService
from handlers import g_sensor
from service.functions import sort_gas_sensors
data1 = GasSensorService.get_archive_values('2024-05-17','насосная.1')
data1 = sort_gas_sensors(data1)
print(data1)
PlotService.plot_gas_level_date(data1)

