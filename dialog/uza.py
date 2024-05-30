from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from states import UzaSG

main = Dialog(
    Window(
        StaticMedia(path=Format('{start_data[path]}'), type=ContentType.PHOTO),
        Cancel(Const('Назад')),
        state=UzaSG.main
    )
)
