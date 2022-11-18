import os
import asyncio
from pyrogram import client, filters
from excel_parsing import parse_excel
from apscheduler.schedulers.asyncio import AsyncIOScheduler

api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)


async def job():
    filename = "users_files/701715759/file_0.xlsx"
    people = await parse_excel(filename)
    async for member in app.get_chat_members(-1001567792707):
        try:
            people.pop("+" + member.user.phone_number)
            print(people["+" + member.user.phone_number])
        except:
            print("Был бы ты человек")
    # for index, elem in enumerate(people):
    #     # Дообавление пользователя в контакты
    #     new_user = await app.import_contacts([
    #         InputPhoneContact(elem, people[elem])
    #     ])
    #     try:
    #         await app.add_chat_members(-1001567792707, new_user.users[0].id)
    #         break
    #     except:
    #         continue
    await asyncio.sleep(1)


async def check_users_files():
    """
    Функция для поиска файлов, добавленных пользователем
    :return: словарь с файлами для каждого пользователя
    """
    users_files = {}
    files_dir = "users_files/"
    for username in os.listdir(files_dir):
        for path in os.listdir(files_dir+username):
            if username in users_files:
                users_files[username].append(f"{files_dir}{username}/{path}")
            else:
                users_files[username] = [f"{files_dir}{username}/{path}"]
    return users_files


# app.run()
scheduler = AsyncIOScheduler()
"""
Бот постоянно будет чекать файлы на сервере, потом проверять по уже запущенным jobам, парсится файл или нет
Проверку по запущенным jobам надо организовать
"""
# parsing_users_files = asyncio.run(check_users_files())
# for user in parsing_users_files:
#     for parsing_file in parsing_users_files[user]:
#         parsing_file = parsing_file

scheduler.add_job(job, "interval", seconds=60)
scheduler.start()
print(scheduler.get_jobs())


