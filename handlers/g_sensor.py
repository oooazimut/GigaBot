from typing import Any
import datetime
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar
from db.repo import GasSensorService
from states import GasSensorsSG


async def to_current_level(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = GasSensorService().get_last_values()
    if data:
        manager.dialog_data['current_level'] = data
        await manager.switch_to(GasSensorsSG.current)
    else:
        await cq.answer('Данные устарели', show_alert=True)
async def on_date_clicked(
        callback: ChatEvent,
        widget: ManagedCalendar,
        manager: DialogManager,
        clicked_date: datetime.date, /):
    data = LosRepo.get_levels(clicked_date)
    if data:
        PlotService.archive_levels(data)
        await manager.switch_to(MainSG.archive)
    else:
        await callback.answer(f'Нет данных за {clicked_date}', show_alert=True)