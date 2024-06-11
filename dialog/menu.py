from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Button
from aiogram_dialog.widgets.text import Const

from handlers.menu import on_pumpwork, on_uza
from states import MenuSG, GasSensorsSG, PressuresSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),

        Start(Const("Газоанализаторы"), state=GasSensorsSG.main, id='gassensors'),
        Start(Const("Манометры"), state=PressuresSG.main, id='manometers'),
        Button(Const('Шкаф УЗА'), id='to_uza', on_click=on_uza),
        Button(Const('Наработка насосов'), id='to_pumpwork', on_click=on_pumpwork),
        state=MenuSG.main
    ),
)
