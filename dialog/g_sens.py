from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel, Back, Button, Select, Column, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from custom.babel_calendar import CustomCalendar
from getters import g_sens
from handlers import g_sensor
from states import GasSensorsSG

g_sens_menu = Dialog(
    Window(
        Const("Газоанализаторы"),
        SwitchTo(Const("Пробная"), state=GasSensorsSG.prob_sens, id="prob_bt"),
        SwitchTo(Const("Насосная"), state=GasSensorsSG.pump_sens, id="pump_id"),
        Cancel(Const("В меню")),
        state=GasSensorsSG.main

    ),
    Window(
        Const("Пробная"),
        Button(Const("Текущие значения"), on_click=g_sensor.to_current_level, id="cur_bt"),
        SwitchTo(Const("Архив"), state=GasSensorsSG.archive, id="arch_bt"),
        SwitchTo(Const("Главное меню"), state=GasSensorsSG.main, id="bc_to_main"),
        state=GasSensorsSG.prob_sens
    ),
    Window(
        Const("Текущее значение:"),
        StaticMedia(path=Format('{dialog_data[path]}'), type=ContentType.PHOTO),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=GasSensorsSG.main),
        state=GasSensorsSG.current
    ),
    Window(
        Const('Выберите дату:'),
        CustomCalendar(id='cal', on_click=g_sensor.on_date_click_prob),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=GasSensorsSG.prob_sens),
        state=GasSensorsSG.archive
    ),
    Window(
        Const("Все датчики на один график или по отдельности"),
        SwitchTo(Const("Выбор датчика"), id="one_sens", state=GasSensorsSG.choice_sens),
        SwitchTo(Const("Все в одном"), id="all_sens", state=GasSensorsSG.plot, on_click=g_sensor.on_allprob),
        Cancel(Const("Главное меню")),
        state=GasSensorsSG.choice_g_sens
    ),
    Window(
        Const("Выбор номера датчика:"),
        Column(
            Select(
                Format('{item[0]} {item[1]}'),
                id='sens_choice',
                items='g_sens',
                item_id_getter=lambda x: x[0],
                on_click=g_sensor.on_sens_selected
            )
        ),
        SwitchTo(Const("Назад"), id='to_main_gas', state=GasSensorsSG.choice_g_sens),
        Cancel(Const("Главное меню")),
        state=GasSensorsSG.choice_sens,
        getter=g_sens.on_sens_prob_selected
    ),
    Window(
        StaticMedia(path=Format('{dialog_data[path]}'), type=ContentType.PHOTO),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=GasSensorsSG.choice_g_sens),
        Cancel(Const('Главное меню')),
        state=GasSensorsSG.plot
    ),
    Window(
        Const("Насосная"),
        Button(Const("Текущее значение"), on_click=g_sensor.to_current_g_pump_level, id='p_val_sens'),
        SwitchTo(Const("Архив"), state=GasSensorsSG.archive_pumps, id='p_archive'),
        SwitchTo(Const("Главное меню"), state=GasSensorsSG.main, id='back_bt'),
        state=GasSensorsSG.pump_sens
    ),
    Window(
        Const('Выберите дату:'),
        CustomCalendar(id='cal', on_click=g_sensor.on_date_clicked),
        SwitchTo(Const('Назад'), id='to_main_pressure', state=GasSensorsSG.pump_sens),
        state=GasSensorsSG.archive_pumps
    ),
    Window(
        Const("Все датчики на один график или по отдельности"),
        SwitchTo(Const("Выбор датчика"), id="one_sens_pump", state=GasSensorsSG.choice_sens_pump),
        SwitchTo(Const("Все в одном"), id="all_sens", state=GasSensorsSG.plot, on_click=g_sensor.on_allinone),
        Cancel(Const("Главное меню")),
        state=GasSensorsSG.choice_p_gsens
    ),
    Window(
        Const("Выбор номера датчика:"),
        Column(
            Select(
                Format('{item[0]} {item[1]}'),
                id='sens_choice',
                items='p_sens',
                item_id_getter=lambda x: x[0],
                on_click=g_sensor.on_sens_selected
            )
        ),
        SwitchTo(Const("Назад"), id='to_main_gas', state=GasSensorsSG.choice_p_gsens),
        Cancel(Const("Главное меню")),
        state=GasSensorsSG.choice_sens_pump,
        getter=g_sens.on_sens_selected
    ),

)
