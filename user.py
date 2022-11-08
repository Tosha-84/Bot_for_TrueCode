from pyrogram import client, filters
from pyrogram.types import InputPhoneContact
# import excel_parsing
from excel_parsing import parse_excel

from datetime import datetime, timedelta
from pyrogram.types import ChatPermissions

#app = client.Client("my_account")

api_id = 24648483
api_hash = "9260bd2eba93540061e9aef0f518ea7e"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)

q = 0
#
@app.on_message(filters.me)
async def echo(client, message):
    await message.reply_text(message.text)
    people = await parse_excel("numbers.xlsx")
    print(people)
    print(type(people))

    print("Прочёсывание")
    for index, elem in enumerate(people):
        print(elem)

    # await message.reply_text(message.text)
    #
    # count = await app.get_contacts_count()
    # print("До:", count)
    #
    # new_user = await app.import_contacts([
    #     InputPhoneContact("+7-984-274-0104", "Делечка")
    # ])
    # print(new_user.users[0].id)
    #
    # count = await app.get_contacts_count()
    # print("После:", count)

    # id Дели
    # 701715759
    # await app.add_chat_members(-1001567792707, 701715759)









# async def main():
#     async with client.Client("my_account", api_id, api_hash) as app:
#         await app.send_message("me", "Greetings from **Pyrogram**!")


app.run()





# async def main():
#     async with client.Client("my_account", api_id, api_hash) as app:
#         await app.send_message("me", "Greetings from **Pyrogram**!")
#
#
# client.asyncio.run(main())
