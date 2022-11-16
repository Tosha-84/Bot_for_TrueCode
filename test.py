import telebot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from test1 import start_bot

from telebot.async_telebot import AsyncTeleBot


# API_TOKEN = '1986393023:AAGmgNDQVTn_MmBBP1Y8DMJqLVSxwvQOvV8'
API_TOKEN = '5648589910:AAFArjtVL_BcnCKzRbJcKRpnlfRJV97YLWo'
# bot = telebot.TeleBot(API_TOKEN)
bot = AsyncTeleBot(API_TOKEN)


# api_id = 24648483
# api_hash = "9260bd2eba93540061e9aef0f518ea7e"
# app = client.Client("my_account", api_id=api_id, api_hash=api_hash)


async def String_to_Command(string):
    while string.find(' ') != -1:
        string = '/' + string[0:string.find(' ')] + '_' + string[string.find(' ') + 1:len(string)]
    print(string)
    return string


async def make_markup_wo_upload_file():
    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
    buttonC = telebot.types.InlineKeyboardButton('Начать добавление', callback_data='start')
    buttonD = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.row(buttonC, buttonA)
    markup.row(buttonD)

    return markup


async def make_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
    buttonB = telebot.types.InlineKeyboardButton('Загрузить документ с номерами', callback_data='upload')
    buttonC = telebot.types.InlineKeyboardButton('Начать добавление', callback_data='start')
    buttonD = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.row(buttonB)
    markup.row(buttonC, buttonA)
    markup.row(buttonD)

    return markup


# Handle '/start'
@bot.message_handler(commands=['start'])
async def start_message(message):
    """
    :param message: class 'telebot.types.Message'
    Обработчик команды start, выдает пользователю меню для выбора дальнейших действий
    """
    await bot.send_message(message.chat.id, '\U00002694    Привет! Я позволю тебе управлять добавлением пользователей в канал'
                                      'телеграм из файла. \n'
                                      '\U00002694    Для удобства пользования не нужно отправлять мне сообщения '
                                      '(за исключениемм файлов), достаточно делать выбор из предложенных'
                                      'вариантов.')

    markup = await make_markup()

    await bot.send_message(message.chat.id, 'Выберите необходимый пункт',
                     reply_markup=markup)


@bot.message_handler(content_types=['document'])
async def get_file(message):
    file_name = message.document.file_name
    file_extension = file_name.split('.')[-1]
    if file_extension != 'xlsx':
        markup = make_markup()
        bot.send_message(message.chat.id, 'Бот умеет обрабатывать только xlsx файлы(', reply_markup=markup)
    else:
        file_info = await bot.get_file(message.document.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        with open(f"{message.chat.id}_file.xlsx", 'wb') as new_file:
            new_file.write(downloaded_file)
        markup = await make_markup_wo_upload_file()
        await bot.send_message(message.chat.id, 'Файл успешно загружен', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
async def handle(call):
    # global app
    if call.data == 'start':

        # scheduler = AsyncIOScheduler()
        filename = f"{call.message.chat.id}_file.xlsx"
        # scheduler.add_job(job, "interval", args=[filename], seconds=60)
        # scheduler.start()
        # await app.run()
        # asyncio.run(start_bot(filename))
        await asyncio.gather(start_bot(filename))

    elif call.data == 'stop':
        print()
    elif call.data == 'upload':
        await bot.send_message(chat_id=call.message.chat.id, text='Загрузите файл в формате xlsx')
    elif call.data == 'settings':
        print()
        markup = telebot.types.InlineKeyboardMarkup()
        button20 = telebot.types.InlineKeyboardButton('20', callback_data='amount')
        button50 = telebot.types.InlineKeyboardButton('50', callback_data='amount')
        button100 = telebot.types.InlineKeyboardButton('100', callback_data='amount')
        button150 = telebot.types.InlineKeyboardButton('150', callback_data='amount')
        button200 = telebot.types.InlineKeyboardButton('200', callback_data='amount')
        button250 = telebot.types.InlineKeyboardButton('250', callback_data='amount')

        markup.row(button20, button50)
        markup.row(button100, button150)
        markup.row(button200, button250)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите'
                                                                                                     'лимит добавления'
                                                                                                     'количества'
                                                                                                     'пользователей',
                              reply_markup=markup)
    elif call.data == 'amount':
        markup = telebot.types.InlineKeyboardMarkup()
        buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
        buttonB = telebot.types.InlineKeyboardButton('Загрузить документ с номерами', callback_data='upload')
        buttonC = telebot.types.InlineKeyboardButton('Начать добавление', callback_data='start')
        buttonD = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')

        markup.row(buttonB)
        markup.row(buttonC, buttonA)
        markup.row(buttonD)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите'
                                                                                                     'необходимый'
                                                                                                     'пункт',
                              reply_markup=markup)


# bot.polling()
# bot.poll_handlers()

import asyncio
asyncio.run(bot.polling())
