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



async def job(message='stuff', n=1):
    print("Asynchronous invocation (%s) of I'm working on:" % n, message)


    # await message.reply_text(message.text)
    people = await parse_excel("numbers.xlsx")
    print(people)
    print(type(people))

    async for member in app.get_chat_members(-1001567792707):
        print(member)
        try:
            print("+" + member.user.phone_number)
        except:
            print("Это бот")

        # people.pop("+" + member.user.phone_number)

        try:
            people.pop("+" + member.user.phone_number)
            print(people["+" + member.user.phone_number])
        except:
            print("Был бы ты человек")
    # print(type(users))
    print(people)


    print("Прочёсывание")
    for index, elem in enumerate(people): # index может помочь с прочёсыванием не с нуля
        print(elem)
        print(people[elem])

        count = await app.get_contacts_count()
        print("До:", count)

        new_user = await app.import_contacts([
            InputPhoneContact(elem, people[elem])
        ])
        print(new_user.users[0].id)

        count = await app.get_contacts_count()
        print("После:", count)

        await app.add_chat_members(-1001567792707, new_user.users[0].id)





    asyncio.sleep(1)

for i in range(1, 2):
    schedule.every(20).seconds.do(job, n=i)
schedule.every(5).to(10).days.do(job)
schedule.every().hour.do(job, message='things')
schedule.every().day.at("10:30").do(job)

loop = asyncio.get_event_loop()
while True:
    app.run()
    loop.run_until_complete(schedule.run_pending())
    time.sleep(0.1)
