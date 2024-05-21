from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from db.repo import PressureService
from states import PressuresSG


async def to_current_pressures(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PressureService.get_last_values()
    if data:
        manager.dialog_data['current_pressures'] = data
        await manager.switch_to(PressuresSG.current)
    else:
        await cq.answer('Данные устарели', show_alert=True)


def to_pressures_archive(cq: CallbackQuery, button: Button, manager: DialogManager):
    pass


def on_pump_selected(cq: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    pass
