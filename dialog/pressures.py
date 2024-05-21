from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Select
from aiogram_dialog.widgets.text import Const

from handlers.pressures import to_current_pressures, to_pressures_archive, on_pump_selected
from states import PressuresSG

main_pressure = Dialog(
    Window(
        Const("Манометры"),
        Button(Const("Текущие значения"), id='to_current', on_click=to_current_pressures),
        SwitchTo(Const('Архив'), id='to_pump_choice'),
        state=PressuresSG.main

    ),
    Window(
        Const("Текущие значения"),
        state=PressuresSG.current
    ),
    Window(
        Const("Выбор насоса:"),
        Select(
            items='pumps',
            on_click=on_pump_selected,
        ),
        state=PressuresSG.pump_choise
    ),

)
