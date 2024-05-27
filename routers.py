from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states import MenuSG

start_router = Router()

@start_router.message(CommandStart())
async def bot_starter(msg: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.main, mode=StartMode.RESET_STACK)
