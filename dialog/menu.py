from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
from states import menuSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Button(Const("Газоанадлизаторы"), id='gaz_sensor', start=g_sensor),
        Button(Const("Манометры"), id='pressure_gauge', state=p_gauge),
        Button(Const("УЗА"), id='uza', state=s_uza),
        Button(Const('Доступность приборов'), id='availability', state=availab),
        Button(Const("Наработка моторов"), id='operating_time', state=oper_time),
        state=menuSG.main
    ),
)