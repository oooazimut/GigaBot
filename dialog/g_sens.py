from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
from states import G_sensSG

g_sens_menu = Dialog(
    Window(
        Const("Газоанализаторы"),
        Button(Const("Пробная"), on_click=Start(state=G_sensSG.prob_sens,id="prob_bt")),
        Button(Const("Насосная"), on_click=Start(state=G_sensSG.pump_sens, id="pump_id")),
        state=G_sensSG.main
    ),
    Window(
        Const("Пробная"),
        Button(Const("Текущие значения"), on_click=Start( state= G_sensSG.current, id="cur_bt")),
        Button(Const("Архив"), id='achive', on_click= Start(state= G_sensSG.archive, id="arch_bt")),
        state=G_sensSG.prob_sens
    ),
    Window(
        Const("Текущее значение:"),

        state=G_sensSG.current
    ),
    Window(
        Const("Архив"),

        state=G_sensSG.archive
    ),
    Window(
        Const("Насосная"),
        Button(Const("Текущее значение"), on_click=Start(state= , id='p_val_sens')),
        Button(Const("Архив"),on_click=Start(state=G_sensSG.archive, id='')),
        state=G_sensSG.pump_sens
    ),
    Window(
        Const("Текущее значение"),
        state=G_sensSG.p_val_sens
    ),
    Window(
        Const("Архив"),
        state=G_sensSG.archive
    )
)
