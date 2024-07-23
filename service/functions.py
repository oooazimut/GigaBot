from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from db.repo import UserService

from mybot import MyBot

def chunks(array: list, chunk: int):
    for i in range(0, len(array), chunk):
        yield array[i : i + chunk]


def convert_to_bin(num: int, zerofill: int) -> str:
    return bin(num)[2:].zfill(zerofill)[::-1]


def sort_pressures_by_pumps(data):
    result = dict()
    for item in data:
        result.setdefault(item["name"], []).append((item["dttm"], item["value"]))

    return result


def sort_gas_sensors(data):
    result = dict()
    for item in data:
        result.setdefault(item["name"], []).append((item["dttm"], item["value"]))

    return result


async def send_message(text: str, userids: list | None = None):
    bot: Bot = MyBot.get_instance()
    if not userids:
        userids = UserService.get_all_users()

    for user in userids:
        try:
            await bot.send_message(chat_id=user, text=text)
        except TelegramBadRequest:
            pass
