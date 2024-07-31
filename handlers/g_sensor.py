import datetime
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar

from config import GAS_SENS_DESCS, GAS_SENS_PROB_DESCS
from db.repo import GasSensorService
from service.functions import sort_gas_sensors
from service.plot import PlotService
from states import GasSensorsSG, SensPlotSG


async def to_current_level(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = GasSensorService.get_last_values()
    if data:
        manager.dialog_data["path"] = PlotService.plot_current_gas_level_prob(data)
        await manager.switch_to(GasSensorsSG.current)
    else:
        await cq.answer("Данные устарели, прибор не на связи.", show_alert=True)


async def to_current_g_pump_level(
    cq: CallbackQuery, button: Button, manager: DialogManager
):
    data = GasSensorService.get_last_values()
    if data:
        manager.dialog_data["path"] = PlotService.plot_current_gas_level_pumps(data)
        await manager.switch_to(GasSensorsSG.current)
    else:
        await cq.answer("Данные устарели, прибор не на связи.", show_alert=True)


async def on_date_clicked(
    callback: CallbackQuery,
    widget: ManagedCalendar,
    manager: DialogManager,
    clicked_date: datetime.date,
    /,
):
    data = GasSensorService.get_archive_values(clicked_date)
    if data:
        date_str = clicked_date.strftime("%Y-%m-%d")
        manager.dialog_data["date"] = date_str
        await manager.switch_to(GasSensorsSG.choice_p_gsens)
    else:
        await callback.answer("Нет данных за этот день", show_alert=True)


async def on_date_click_prob(
    event: CallbackQuery,
    widget: ManagedCalendar,
    dialog_manager: DialogManager,
    date: datetime.date,
    /,
) -> Any:
    data = GasSensorService.get_archive_values(date)
    if data:
        date_str = date.strftime("%Y-%m-%d")
        dialog_manager.dialog_data["date"] = date_str
        await dialog_manager.switch_to(GasSensorsSG.choice_g_sens)
    else:
        await event.answer("Нет данных за этот день", show_alert=True)


async def on_sens_selected(
    cq: CallbackQuery, widget: Any, manager: DialogManager, g_sens: str
):
    data = GasSensorService.get_archive_values(
        manager.dialog_data["date"], g_sens=[g_sens]
    )
    sorted_data = sort_gas_sensors(data)
    data = {"path": PlotService.plot_gas_level_date(sorted_data)}
    await manager.start(SensPlotSG.main, data=data)


async def on_allinone(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = GasSensorService.get_archive_values(manager.dialog_data["date"], GAS_SENS_DESCS)
    sorted_data = sort_gas_sensors(data)
    data = {"path": PlotService.plot_gas_level_date(sorted_data)}
    await manager.start(SensPlotSG.main, data=data)


async def on_allprob(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = GasSensorService.get_archive_values(manager.dialog_data["date"], GAS_SENS_PROB_DESCS)
    sorted_data = sort_gas_sensors(data)
    data = {"path": PlotService.plot_gas_level_date(sorted_data)}
    await manager.start(SensPlotSG.main, data=data)
