from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from states import G_sensSG, Press_sensSG, UzaSG, Avail_SG, Engine_operatingSG


async def gaz_sensor(callback_query: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(G_sensSG.main)

async def pressure_sensor(callback_query: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(Press_sensSG.main)

async def uza(callback_query: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(UzaSG.main)

async def availability(callback_query: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(Avail_SG.main)

async def engine_operating(callback_query: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(Engine_operatingSG.main)