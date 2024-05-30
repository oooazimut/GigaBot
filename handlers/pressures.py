import datetime
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar

from db.repo import PressureService
from service.functions import sort_pressures_by_pumps
from service.plot import PlotService
from states import PressuresSG


async def to_current(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PressureService.get_last_values()
    if data:
        pressures = [round(i['value'], 1) for i in data]
        p3 = pressures.pop()
        pressures.insert(2, p3)
        pressures.reverse()
        manager.dialog_data['path'] = PlotService.plot_current_pump(pressures, 'Давление (бар)')
        await manager.switch_to(PressuresSG.plot)
    else:
        await cq.answer('Данные устарели, прибор не на связи.', show_alert=True)


async def on_pump_selected(cq: CallbackQuery, widget: Any, manager: DialogManager, pump: str):
    data = PressureService.get_values_by_date(manager.dialog_data['date'], pump=pump)
    sorted_data = sort_pressures_by_pumps(data)
    manager.dialog_data['path'] = PlotService.plot_pressures_by_date(sorted_data)
    await manager.switch_to(PressuresSG.plot)


async def on_date(callback: ChatEvent, widget: ManagedCalendar, manager: DialogManager, clicked_date: datetime.date, /):
    data= PressureService.get_values_by_date(clicked_date)
    if data:
        date_str = clicked_date.strftime('%Y-%m-%d')
        manager.dialog_data['date'] = date_str
        await manager.switch_to(PressuresSG.quantity_choice)
    else:
        await callback.answer('Нет данных за этот день', show_alert=True)

async def on_allinone(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PressureService.get_values_by_date(manager.dialog_data['date'])
    sorted_data = sort_pressures_by_pumps(data)
    manager.dialog_data['path'] = PlotService.plot_pressures_by_date(sorted_data)
