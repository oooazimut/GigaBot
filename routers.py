from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from db.repo import UserService
from states import MenuSG, VerifySG

start_router = Router()


@start_router.message(CommandStart())
async def bot_starter(msg: Message, dialog_manager: DialogManager):
    user = UserService.get_user(msg.from_user.id)
    if user:
        await dialog_manager.start(state=MenuSG.main, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(state=VerifySG.main, mode=StartMode.RESET_STACK)
