from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo, Select, Button, Back, Column, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from getters.pressures import pumps_choice_getter
from handlers.pressures import on_pump_selected, to_current
from states import PressuresSG

main_pressure = Dialog(
    Window(
        Const("Манометры"),
        Button(Const('Текущие значения'), id='to_current', on_click=to_current),
        SwitchTo(Const('Архив'), id='to_pump_choice', state=PressuresSG.pump_choise),
        state=PressuresSG.main

    ),
    Window(
        Const("Текущие значения"),
        StaticMedia(path='media/current_pressures.png', type=ContentType.PHOTO),
        Back(Const('Назад')),
        state=PressuresSG.current,
    ),
    Window(
        Const("Выбор насоса:"),
        Column(
            Select(
                Format('{item[0]} {item[1]}'),
                id='pumps_choice',
                item_id_getter=lambda x: x[0],
                items='pumps',
                on_click=on_pump_selected,
            )
        ),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=PressuresSG.main),
        Cancel(Const('Главное меню')),
        state=PressuresSG.pump_choise,
        getter=pumps_choice_getter
    )
)
