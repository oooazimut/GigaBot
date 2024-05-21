from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column, SwitchTo
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
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
        SwitchTo(Const("Текущие значения"), state= GasSensorsSG.current, id="cur_bt"),
        SwitchTo(Const("Архив"), state= GasSensorsSG.archive, id="arch_bt"),
        Back(Const("Назад")),
        state=GasSensorsSG.prob_sens
    ),
    Window(
        Const("Текущее значение:"),

        state=GasSensorsSG.current
    ),
    Window(
        Const("Архив"),

        state=GasSensorsSG.archive
    ),
    Window(
        Const("Насосная"),
        Button(Const("Текущее значение"), on_click=Start(state=GasSensorsSG.p_val_sens , id='p_val_sens')),
        Button(Const("Архив"),on_click=Start(state=GasSensorsSG.archive, id='p_archive')),
        state=GasSensorsSG.pump_sens
    ),
    Window(
        Const("Текущее значение:"),
        state=GasSensorsSG.prob_sens
    ),
    Window(
        Const("Архив"),
        state=GasSensorsSG.archive
    )
)
