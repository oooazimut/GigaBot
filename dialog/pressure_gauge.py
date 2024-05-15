from aiogram import F
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Start, Cancel, Back, Button, Select, Column
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

pressure_dialog = Dialog(
    Window(
        Const("Манометры"),
        Button(Const("Текущие значения"), id='press_val', state=),
        Button(Const("Архив"))

    ),
    Window(
        Const("Текущие значения"),
        state=
    ),
    Window(
        Const("Архив"),
        state=
    )
)