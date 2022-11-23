import os
from os import path
import asyncio
from pyrogram import client, filters
from pyrogram import idle
from pyrogram.types import InputPhoneContact
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

async def job():
    # Старт клиента
    print("check")
    await app.start()
    # Проверка на наличие файла и создание словаря из тех, кого ещё нет в канале
    if os.path.isfile('D:/Projects/Bot_for_TrueCode/users_files/484704240/file_0.xlsx'):
        print("Проверка сработала")
        # await app.send_message(-1001567792707, "Hello")
        people = await parse_excel("users_files/484704240/file_0.xlsx")
        # print(people)
        async for member in app.get_chat_members(-1001567792707):
            # print(member)
            people.pop("+" + member.user.phone_number)
        print(people)

        # Проверка на то, остались ли в файле те, кого нужно добавить
        if len(people) == 0:
            print("Тут нужно удалить файл")
        else:
            # Само добавление (может поменяю, но пока пусть так)
            for index, elem in enumerate(people):
                # Дообавление пользователя в контакты
                new_user = await app.import_contacts([
                    InputPhoneContact(elem, people[elem])
                ])
                try:
                    await app.add_chat_members(-1001567792707, new_user.users[0].id)
                    await app.send_message(-1001567792707, "@" + new_user.users[0].username + ", Hello!")
                    break
                except:
                    continue
    else:
        print("Файл отсутствует")
    await app.stop()


async def check_users_files(schedule):
    # await app.start()
    global users_files
    """
    Функция для поиска файлов, добавленных пользователем
    :return: словарь с файлами для каждого пользователя
    """

    # files_dir = "users_files/"
    # for username in os.listdir(files_dir):
    #     print(username)
    #     for path in os.listdir(files_dir+username):
    #         print("Если файлов нет")
    #         if username in users_files:
    #             print("Если файлов нет")
    #             continue
    #         else:
    #             file_path = f"{files_dir}{username}/{path}"
    #             parse_time = 10
    #
    #             # schedule.add_job(check_users_files, "interval", args=[schedule], seconds=parse_time)
    #             schedule.add_job(job, "interval", args=[file_path], seconds=parse_time)
    #
    #             users_files[username] = [file_path]


    parse_time = 20
    schedule.add_job(job, "interval", seconds=parse_time)

    print("Тут проходит")
    schedule.start()
    print("Включение idle")
    await idle()
    print(users_files)

    # app.run()

    # print(users_files['484704240'])
    # await job(users_files['484704240'][0])
    return users_files


# app.run(job('D:/Projects/Bot_for_TrueCode/users_files/484704240/file_0.xlsx'))
scheduler = AsyncIOScheduler()
# asyncio.run(check_users_files(scheduler))
app.run(check_users_files(scheduler))

