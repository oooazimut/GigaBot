from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from states import MenuSG, GasSensorsSG, PressuresSG, UzaSG, AvailSG, PumpWorkSG

main_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Start(Const("Газоанализаторы"), state=GasSensorsSG.main, id='gassensors'),
        Start(Const("Манометры"), state=PressuresSG.main, id='manometers'),
        Start(Const("УЗА"), state=UzaSG.main, id='uza'),
        Start(Const('Доступность приборов'), state=AvailSG.main, id='pravailability'),
        Start(Const("Наработка насосов"), state=PumpWorkSG.main, id='pumpwork'),
        state=MenuSG.main
    ),
)
