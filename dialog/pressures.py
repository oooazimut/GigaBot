from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo, Select, Button, Column, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from custom.babel_calendar import CustomCalendar
from getters.pressures import pumps_choice_getter
from handlers.pressures import on_pump_selected, to_current, on_date, on_allinone
from states import PressuresSG

main = Dialog(
    Window(
        Const("Манометры"),
        Button(Const('Текущие значения'), id='to_current', on_click=to_current),
        SwitchTo(Const('Архив'), id='to_date_choice', state=PressuresSG.date_choice),
        Cancel(Const('Главное меню')),
        state=PressuresSG.main
    ),
    Window(
        Const('Выбор даты:'),
        CustomCalendar(id='cal', on_click=on_date),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=PressuresSG.main),
        Cancel(Const('Главное меню')),
        state=PressuresSG.date_choice
    ),
    Window(
        Const('Все насосы одним графиком или какой-то один насос?'),
        SwitchTo(Const('Выбор насоса'), id='to_pump_choice', state=PressuresSG.pump_choice),
        SwitchTo(Const('Все в одном'), id='all_in_one', state=PressuresSG.plot, on_click=on_allinone),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=PressuresSG.main),
        Cancel(Const('Главное меню')),
        state=PressuresSG.quantity_choice
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
        state=PressuresSG.pump_choice,
        getter=pumps_choice_getter
    ),
    Window(
        StaticMedia(path=Format('{dialog_data[path]}'), type=ContentType.PHOTO),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=PressuresSG.main),
        Cancel(Const('Главное меню')),
        state=PressuresSG.plot
    ),

)
