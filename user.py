from pyrogram import client, filters
from pyrogram.types import InputPhoneContact
import schedule
import time
# import excel_parsing
from excel_parsing import parse_excel
import asyncio

from datetime import datetime, timedelta
from pyrogram.types import ChatPermissions

# app = client.Client("my_account")

api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)

q = 0


@app.on_message(filters.me)
async def echo(client, message):
    await message.reply_text(message.text)
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
        # print(elem)
        # print(people[elem])

        count = await app.get_contacts_count()
        # print("До:", count)

        new_user = await app.import_contacts([
            InputPhoneContact(elem, people[elem])
        ])
        # print(new_user.users[0].id)

        count = await app.get_contacts_count()
        # print("После:", count)

        await app.add_chat_members(-1001567792707, new_user.users[0].id)
        break

async def echo(client):
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
    for index, elem in enumerate(people): # index может помочь с прочёсыванием не с нуля
        # print(elem)
        # print(people[elem])

        count = await app.get_contacts_count()
        # print("До:", count)

        new_user = await app.import_contacts([
            InputPhoneContact(elem, people[elem])
        ])
        # print(new_user.users[0].id)

        count = await app.get_contacts_count()
        # print("После:", count)

        await app.add_chat_members(-1001567792707, new_user.users[0].id)
        break

async def main():
    async with client.Client("my_account", api_id, api_hash) as app:
        # client.Client.start()
        while True:
            await app.send_message("me", "Greetings from **Pyrogram**!")
            await echo(client)
            await asyncio.sleep(10)



asyncio.run(main())



# app.run()
