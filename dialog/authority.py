from aiogram import F
from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

import config
from db.repo import UserService
from states import VerifySG, MenuSG


async def pass_is_right(msg: Message, widget: MessageInput, manager: DialogManager):
    UserService.insert_user(msg.from_user.id, msg.from_user.full_name)
    await manager.start(state=MenuSG.main, mode=StartMode.RESET_STACK)


main = Dialog(
    Window(
        Const('Введите пароль:'),
        MessageInput(content_types=ContentType.TEXT, func=pass_is_right, filter=F.text == config.PASSWORD),
        state=VerifySG.main
    )
)
