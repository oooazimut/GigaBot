from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

import vars
from config import PUMPS_IDS
from db.repo import PumpWorkService
from service.functions import convert_to_bin
from service.plot import PlotService
from states import PumpWorkSG, UzaSG


async def on_pumpwork(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PumpWorkService.get_current()
    data = [round(int(val) / 3600, 1) for val in data]
    plot_path = PlotService.plot_current_pump(data, 'Наработка (часы)')
    await manager.start(state=PumpWorkSG.main, data={'path': plot_path})


async def on_uza(cq: CallbackQuery, button: Button, manager: DialogManager):
    uzas = map(int, convert_to_bin(vars.uzas, zerofill=6))
    uzas = list(enumerate(uzas, start=1))
    permissions = map(int, convert_to_bin(vars.permissions, zerofill=4))
    permissions = list(zip(PUMPS_IDS, permissions))
    permissions.reverse()
    permissions[0] = ('Н-2.*', permissions[0][1])
    pumps = map(int, convert_to_bin(vars.pumps, zerofill=5))
    pumps = list(zip(PUMPS_IDS, pumps))
    pumps.reverse()
    data = {
        'УЗА': uzas,
        'Разрешения': permissions,
        'Насосы': pumps
    }
    plot_path = PlotService.plot_uza(data)
    await manager.start(UzaSG.main, data={'path': plot_path})

