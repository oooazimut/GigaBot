from aiogram_dialog import Dialog, Window

from getters.pumpwork import current_getter
from states import PumpWorkSG

main = Dialog(
    Window(
        state=PumpWorkSG.main,
        getter=current_getter
    )
)