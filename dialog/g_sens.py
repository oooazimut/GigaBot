from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
from states import g_sensSG

g_sens_menu = Dialog(
    Window(
        Const("Газоанализаторы"),
        Button(Const("Пробная"), id='g_sens_pr', state=),
        Button(Const("Насосная"), id='g_sens_ns', state=),
        state=g_sens_menu.main
    ),
),

g_sens_prob = Dialog(
    Window(
        Const("Пробная"),
        Button(Const("Текущие значения"), id='g_val_prob', state=g_sensSG.prob_sens),
        Button(Const("Архив"), id='achive', state=achive),
        state=g_sensSG.main
    ),
    Window(
        state=prob_sens
    ),
    Window(
        state=archive
    )
),
