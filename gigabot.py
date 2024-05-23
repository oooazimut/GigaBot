import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from redis.asyncio import Redis

import config
from dialog import menu, pressures
import jobs
import middlewares
from custom.media_storage import MediaIdStorage


async def main():
    bot = Bot(config.TOKEN)
    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(jobs.save_data, 'interval', seconds=5, id='savedata')
    scheduler.add_job(jobs.save_pumpwork, 'cron', hour=9, id='savepumpwork')
    storage = RedisStorage(Redis(), key_builder=DefaultKeyBuilder(with_destiny=True, with_bot_id=True))
    dp = Dispatcher(storage=storage)
    dp.update.outer_middleware(middlewares.DataMiddleware({'scheduler': scheduler}))
    dp.include_router(menu.main_dialog)
    dp.include_router(pressures.main_pressure)
    setup_dialogs(dp, media_id_storage=MediaIdStorage())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
