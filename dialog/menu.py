from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from handlers import menu_handler
from states import MenuSG, G_sensSG, Press_sensSG, UzaSG, Avail_SG, Engine_operatingSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Start(Const("Газоанадлизаторы"), G_sensSG.main),
        Start(Const("Манометры"), Press_sensSG.main),
        Start(Const("УЗА"), UzaSG.main),
        Start(Const('Доступность приборов'), Avail_SG.main),
        Start(Const("Наработка моторов"), Engine_operatingSG.main),
        state=MenuSG.main
    ),
)