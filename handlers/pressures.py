from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from db.repo import PressureService
from service.plot import PlotService
from states import PressuresSG


async def to_current(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PressureService.get_last_values()
    if data:
        pressures = [round(i['value'], 1) for i in data]
        p3 = pressures.pop()
        pressures.insert(2, p3)
        PlotService.plot_current_pressures(pressures)
        await manager.switch_to(PressuresSG.current)
    else:
        await cq.answer('Данные устарели, прибор не на связи.', show_alert=True)


async def to_pressures_archive(cq: CallbackQuery, button: Button, manager: DialogManager):
    pass


async def on_pump_selected(cq: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    pass
