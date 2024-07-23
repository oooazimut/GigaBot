from aiogram import Bot
from db.repo import UserService
from mybot import MyBot
from service.functions import convert_to_bin

tanks = dict(enumerate(convert_to_bin(4, 3), start=1))
conditions = {"0": "норма", "1": "полная!"}
bot: Bot = MyBot.get_instance()
text = "Утренняя сводка:\n\n"
userids = [user.get('id') for user in UserService.get_all_users()]
print(userids)

text += "Уровни:\n"
for tank in tanks:
    text += f"Ёмкость {tank}: {conditions.get(tanks[tank])}\n"

print(text)
