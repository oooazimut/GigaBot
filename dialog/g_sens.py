from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column, SwitchTo
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
from custom.babel_calendar import CustomCalendar
from handlers import g_sensor
from states import GasSensorsSG

g_sens_menu = Dialog(
    Window(
        Const("Газоанализаторы"),
        SwitchTo(Const("Пробная"),state=GasSensorsSG.prob_sens,id="prob_bt"),
        SwitchTo(Const("Насосная"), state=GasSensorsSG.pump_sens, id="pump_id"),
        Cancel(Const("В меню")),
        state=GasSensorsSG.main


    ),
    Window(
        Const("Пробная"),
        Button(Const("Текущие значения"), on_click=g_sensor.to_current_level, id="cur_bt"),
        Button(Const("Архив"), on_click=, id="arch_bt"),
        Back(Const("Назад")),
        state=GasSensorsSG.prob_sens
    ),
    Window(
        Const("Текущее значение:"),

        Back(Const("Назад")),
        state=GasSensorsSG.current
    ),
    Window(
        Const('Выберите дату:'),
        CustomCalendar(id='cal', on_click=handlers.on_date_clicked),

        Back(Const("Назад")),
        state=GasSensorsSG.archive
    ),
    Window(
        Const("Насосная"),
        SwitchTo(Const("Текущее значение"), state=GasSensorsSG.p_val_sens , id='p_val_sens'),
        SwitchTo(Const("Архив"), state=GasSensorsSG.archive, id='p_archive'),
        Back(Const("Назад")),
        state=GasSensorsSG.pump_sens
    ),
    Window(
        Const("Текущее значение:"),

        Back(Const("Назад")),
        state=GasSensorsSG.prob_sens
    ),
    Window(
        Const("Архив"),

        Back(Const("Назад")),
        state=GasSensorsSG.archive
    )
)
