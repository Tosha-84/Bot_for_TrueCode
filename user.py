from pyrogram import client, filters


#app = client.Client("my_account")

api_id = id
api_hash = "hash"
app = client.Client("my_account", api_id=api_id, api_hash=api_hash)

#
@app.on_message(filters.me)
async def echo(client, message):
    # await message.reply_text(message.text)
    await message.reply_text("**sd**")
    # await message.reply_text(app.get_me())





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
