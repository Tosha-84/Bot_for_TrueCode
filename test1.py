import os
import asyncio
from pyrogram import client, filters
from excel_parsing import parse_excel
from apscheduler.schedulers.asyncio import AsyncIOScheduler

api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)

users_files = {}

async def run(filename):
    # await app.start()
    await app.run(await job(filename))
    # await app.stop()

async def job(filename: str):
    await app.start()
    # надо заранее подсчитать количество заполненных строк в эксель файлике и в зависимости от этого выставлять интервал в jobе
    # people = await parse_excel(filename)
    # # print(people)
    # async for member in app.get_chat_members(-1001567792707):
    #     # print(member)
    #     people.pop("+" + member.user.phone_number)
    # print(people)
    await app.stop()



    # TARGET = -1001567792707
    # async with app:
    #     async for member in app.get_chat_members(TARGET):
    #         try:
    #             await people.pop("+" + member.user.phone_number)
    #             print(people["+" + member.user.phone_number])
    #         except:
    #             print("Был бы ты человек")
    #         await print(member)
    #
    # print(people)

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
    # await asyncio.sleep(1)


async def check_users_files(schedule):
    global users_files
    """
    Функция для поиска файлов, добавленных пользователем
    :return: словарь с файлами для каждого пользователя
    """
    files_dir = "users_files/"
    for username in os.listdir(files_dir):
        for path in os.listdir(files_dir+username):
            if username in users_files:
                continue
            else:
                file_path = f"{files_dir}{username}/{path}"
                parse_time = 60
                schedule.add_job(job, "interval", args=[file_path], seconds=parse_time)
                users_files[username] = [file_path]
    scheduler.start()
    print(users_files)
    # print(users_files['484704240'])
    await job(users_files['484704240'][0])
    return users_files


# app.run()
# scheduler = AsyncIOScheduler()
# asyncio.run(check_users_files(scheduler))


