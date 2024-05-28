from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Button
from aiogram_dialog.widgets.text import Const

from handlers.menu import on_pumpwork
from states import MenuSG, GasSensorsSG, PressuresSG, UzaSG, AvailSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),

        Start(Const("Газоанализаторы"), state=GasSensorsSG.main, id='gassensors'),
        Start(Const("Манометры"), state=PressuresSG.main, id='manometers'),
        Start(Const("УЗА"), state=UzaSG.main, id='uza'),
        Start(Const('Доступность приборов'), state=AvailSG.main, id='pravailability'),
        Button(Const('Наработка насосов'), id='to_pumpwork', on_click=on_pumpwork),
        state=MenuSG.main
    ),
)
