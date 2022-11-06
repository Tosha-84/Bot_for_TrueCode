# Библиотека, которая используется для ведения журнала
import logging

import telegram
from telegram import Update, User, Bot
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

# Часть ниже предназначена для ведения журнала, чтобы знать, что и когда не работает должным образом
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Команда start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


# Команда caps, нужно сделать обработчик на пустое сообщение
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not len(context.args):
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Message is empty!')
        return
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# Обработчик на неизвестные команды
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.channel_post.text)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.channel_post.id)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.)


# Эхо (ответ на сообщение тем же сообщением)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    await context.bot.send_message(chat_id=-1001567792707, text=update.message.text)
    await context.bot.send_message(chat_id=-1001567792707, text=update.effective_user.id)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.chat_id)
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.id)



    phone_number = "89025143603"
    #phone_number = "89148891191"

    # print(update.message.chat_id)
    await context.bot.send_contact(-1001567792707, phone_number, "Name")
    await context.bot.send_contact(update.message.chat_id, phone_number, "Name")

    # @Alex_Landers

# string s = "+44....";    //the phone number
# var req2 = await bot.MakeRequestAsync(new SendContact(update.Message.Chat.Id, s, "Name"));
# if(req2.Contact.UserId == 0)
# {
#   Console.WriteLine("The contact does not exist in Telegram");
# }else
# {
#   Console.WriteLine("The contact exists in telegram with UserID:{0}",req2.Contact.UserId.ToString());
# }


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def channel_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)





if __name__ == '__main__':
    application = ApplicationBuilder().token('Здесь Токен').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler((caps_handler))

    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)


    application.run_polling()

