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
        Button(Const("Пробная"), id='g_sens_pr', on_click=),
        Button(Const("Насосная"), id='g_sens_ns', on_click=),
        state=G_sensSG.main
    ),
),

g_sens_prob = Dialog(
    Window(
        Const("Пробная"),
        Button(Const("Текущие значения"), id='g_val_prob', on_click=),
        Button(Const("Архив"), id='achive', on_click=),
        state=G_sensSG.main
    ),
    Window(
        Const("Текущее значение:"),
        state=G_sensSG.prob_sens
    ),
    Window(
        Const("Архив"),
        state=G_sensSG.archive
    )
),
