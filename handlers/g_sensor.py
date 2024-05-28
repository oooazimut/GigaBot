from typing import Any
import datetime
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar
from db.repo import GasSensorService
from service.functions import sort_gas_sensors
from service.plot import PlotService
from states import GasSensorsSG

async def to_current_level(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = GasSensorService.get_last_values()
    if data:
        g_level = [round(i['value'], 1) for i in data]
        p3 = g_level.pop()
        g_level.insert(2, p3)
        manager.dialog_data['path'] = PlotService.plot_current_pressures(g_level)
        await manager.switch_to(GasSensorsSG.current)
    else:
        await cq.answer('Данные устарели, прибор не на связи.', show_alert=True)
async def on_date_clicked(callback: ChatEvent, widget: ManagedCalendar, manager: DialogManager, clicked_date: datetime.date, /):
    data = GasSensorService.get_archive_values(clicked_date)
    if data:
        date_str = clicked_date.strftime('%Y-%m-%d')
        manager.dialog_data['date'] = date_str
        await manager.switch_to(GasSensorsSG.choice_g_sens)
    else:
        await callback.answer('Нет данных за этот день', show_alert=True)
async def on_pump_selected(cq: CallbackQuery, widget: Any, manager: DialogManager, g_sens: str):
    data = GasSensorService.get_archive_values(manager.dialog_data['date'], g_sens=g_sens)
    sorted_data = sort_gas_sensors(data)
    manager.dialog_data['path'] = PlotService.plot_pressures_by_date(sorted_data)
    await manager.switch_to(PressuresSG.plot)