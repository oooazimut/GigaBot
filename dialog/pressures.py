from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from states import PressuresSG

main_pressure = Dialog(
    Window(
        Const("Манометры"),
        Button(Const("Текущие значения"), id='to_current'),
        Button(Const("Архив"), id='to_archive'),
        state=PressuresSG.main

    ),
    Window(
        Const("Текущие значения"),
        state=PressuresSG.current
    ),
    Window(
        Const("Архив"),
        state=PressuresSG.archive
    )
)
