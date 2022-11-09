import asyncio
import aioschedule as schedule
import time


from pyrogram import client, filters
from pyrogram.types import InputPhoneContact
import time
# import excel_parsing
from excel_parsing import parse_excel


api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)


# Одна функция пока что, делить потом буду, когда пойму, как работает библиотека aioschedule
# В ней берётся список подписчиков, словарь из файла, из словаря удаляются подписчики и добавляется первый
async def job(message='stuff', n=1):
    # print("Asynchronous invocation (%s) of I'm working on:" % n, message)
    # await message.reply_text(message.text)

    # Словарь из файла
    people = await parse_excel("numbers.xlsx")

    # print(people)
    # print(type(people))

    # Цикл для удаления подписчиков из файла
    async for member in app.get_chat_members(-1001567792707):
        # print(member)
        try:
            # Сама строчка для удаления, сделано через try, потому что phone_number может быть none
            people.pop("+" + member.user.phone_number)
            print(people["+" + member.user.phone_number])
        except:
            print("Был бы ты человек")
    # print(type(users))
    # print(people)


    print("Прочёсывание")
    for index, elem in enumerate(people): # index может помочь с прочёсыванием не с нуля
        # print(elem)
        # print(people[elem])
        # count = await app.get_contacts_count()
        # print("До:", count)

        # Дообавление пользователя в контакты
        new_user = await app.import_contacts([
            InputPhoneContact(elem, people[elem])
        ])
        # print(new_user.users[0].id)

        # count = await app.get_contacts_count()
        # print("После:", count)

        # Добавление контакта в канал
        await app.add_chat_members(-1001567792707, new_user.users[0].id)

    # Эта строчка здесь просто по аналогии из документации к aioschedule
    asyncio.sleep(1)


# Это было в документации к библиотеке aioschedule
for i in range(1, 2):
    schedule.every(20).seconds.do(job, n=i)
schedule.every(5).to(10).days.do(job)
schedule.every().hour.do(job, message='things')
schedule.every().day.at("10:30").do(job)

loop = asyncio.get_event_loop()
while True:
    app.run() # Вот это где-то должно быть, но я не знаю, где, без этого ошибка о том, что бот не запущен
    loop.run_until_complete(schedule.run_pending())
    time.sleep(0.1)
