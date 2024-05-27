from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from db.repo import PumpWorkService
from service.plot import PlotService
from states import PumpWorkSG


async def on_pumpwork(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PumpWorkService.get_current()
    data = [round(int(val)/3600, 1) for val in data]
    plot_path = PlotService.plot_current_pump(data, 'pumpworks')
    await manager.start(state=PumpWorkSG.main, data={'path': plot_path})