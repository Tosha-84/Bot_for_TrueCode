import telebot
import os
from telebot.async_telebot import AsyncTeleBot

# import test1
# import test2


# API_TOKEN = '1986393023:AAGmgNDQVTn_MmBBP1Y8DMJqLVSxwvQOvV8'
API_TOKEN = '5648589910:AAFArjtVL_BcnCKzRbJcKRpnlfRJV97YLWo'
# bot = telebot.TeleBot(API_TOKEN)
bot = AsyncTeleBot(API_TOKEN)


async def String_to_Command(string):
    while string.find(' ') != -1:
        string = '/' + string[0:string.find(' ')] + '_' + string[string.find(' ') + 1:len(string)]
    print(string)
    return string


async def make_markup_wo_upload_file():
    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
    # buttonD = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')

    markup.row(buttonA)
    # markup.row(buttonD)

    return markup


async def make_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    # buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
    buttonB = telebot.types.InlineKeyboardButton('Загрузить документ с номерами', callback_data='upload')

    markup.row(buttonB)
    # markup.row(buttonA)

    return markup

# @bot.message_handler(content_types=['text'])
# async def message(message):
#     await bot.send_message(message.chat.id, message.text)


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
    files_dir = f"users_files/{message.chat.id}"
    file_name = message.document.file_name
    file_extension = file_name.split('.')[-1]
    if file_extension != 'xlsx':
        markup = make_markup()
        await bot.send_message(message.chat.id, 'Бот умеет обрабатывать только xlsx файлы(', reply_markup=markup)
    else:
        file_info = await bot.get_file(message.document.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        if os.path.exists(files_dir):
            counter = len(os.listdir(files_dir))
            with open(f"{files_dir}/file_{counter}.xlsx", 'wb') as new_file:
                new_file.write(downloaded_file)
        else:
            os.mkdir(files_dir)
            with open(f"{files_dir}/file_0.xlsx", 'wb') as new_file:
                new_file.write(downloaded_file)
        markup = await make_markup_wo_upload_file()
        await bot.send_message(message.chat.id, 'Файл успешно загружен. Сейчас начнется добавление в канал', reply_markup=markup)

        # await test1.job('users_files/484704240/file_0.xlsx')
        # await test1.('users_files/484704240/file_0.xlsx')


@bot.callback_query_handler(func=lambda call: True)
async def handle(call):
    # global app
    if call.data == 'stop':
        try:
            files_dir = f"users_files/{call.message.chat.id}"
            if os.path.exists(files_dir):
                counter = len(os.listdir(files_dir)) - 1
                os.remove(f"{files_dir}/file_{counter}.xlsx")
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Файл удален. Если вы захотите продолжить, то файл придется загрузить заново')
        except:
            await bot.send_message(chat_id=call.message.chat.id, text='К сожалению, файлы не найдены(')
    elif call.data == 'upload':
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Загрузите файл в формате .xlsx')
    elif call.data == 'amount':
        markup = telebot.types.InlineKeyboardMarkup()
        buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
        buttonB = telebot.types.InlineKeyboardButton('Загрузить документ с номерами', callback_data='upload')

        markup.row(buttonB)
        markup.row(buttonA)

        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите'
                                                                                                     'необходимый'
                                                                                                     'пункт',
                              reply_markup=markup)

import asyncio
asyncio.run(bot.polling())
