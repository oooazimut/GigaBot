from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from handlers import menu_handler
from states import MenuSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Button(Const("Газоанадлизаторы"), id='gaz_sensor', on_click= menu_handler.gaz_sensor),
        Button(Const("Манометры"), id='pressure_gauge', on_click= menu_handler.pressure_sensor),
        Button(Const("УЗА"), id='uza', on_click=menu_handler.uza),
        Button(Const('Доступность приборов'), id='availability', on_click= menu_handler.availability),
        Button(Const("Наработка моторов"), id='operating_time', on_click= menu_handler.engine_operating),
        state=MenuSG.main
    ),
)