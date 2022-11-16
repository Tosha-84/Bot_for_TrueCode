import asyncio
from pyrogram import client, filters
from excel_parsing import parse_excel
from apscheduler.schedulers.asyncio import AsyncIOScheduler


api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)


async def job(filename: str):
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


async def start_bot(filename: str):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, "interval", args=[filename], seconds=60)
    scheduler.start()
    app.run()