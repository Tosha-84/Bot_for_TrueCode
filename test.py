import telebot
# import Human
from telebot.types import InputMediaPhoto
# API_TOKEN = '1986393023:AAGmgNDQVTn_MmBBP1Y8DMJqLVSxwvQOvV8'
API_TOKEN = '5648589910:AAFArjtVL_BcnCKzRbJcKRpnlfRJV97YLWo'
bot = telebot.TeleBot(API_TOKEN)


def String_to_Command(string):
    while string.find(' ') != -1:
        string = '/' + string[0:string.find(' ')] + '_' + string[string.find(' ') + 1:len(string)]
    print(string)
    return string


# Handle '/start'
@bot.message_handler(commands=['start'])
def start_message(message):
    # keyboard = telebot.types.ReplyKeyboardMarkup()
    # keyboard.row('Выбрать расу')
    # bot.reply_to(message, 'Привет, если ты здесь, значит тебе нужно Выбрать расу, так давай же начнём',
    #              reply_markup=keyboard)

    bot.send_message(message.chat.id, '\U00002694    Привет! Я позволю тебе управлять добавлением пользователей в канал'
                                      'телеграм из файла. \n'
                                      '\U00002694    Для удобства пользования не нужно отправлять мне сообщения '
                                      '(за исключениемм файлов), достаточно делать выбор из предложенных'
                                      'вариантов.')

    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Остановить добавление', callback_data='stop')
    buttonB = telebot.types.InlineKeyboardButton('Загрузить документ с номерами', callback_data='upload')
    buttonC = telebot.types.InlineKeyboardButton('Начать добавление', callback_data='start')
    buttonD = telebot.types.InlineKeyboardButton('Настройки', callback_data='settings')


    markup.row(buttonB)
    markup.row(buttonC, buttonA)
    markup.row(buttonD)

    bot.send_message(message.chat.id, 'Выберите необходимый пункт',
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Загрузить файл', callback_data='Загрузить файл')


    markup.row(buttonA)

    bot.send_message(message.chat.id, 'Добавить файл',
                     reply_markup=markup)


@bot.message_handler(content_types={'text'})
def fucking_animal(message):
    if message.text == 'Выбрать расу':
        markup = telebot.types.InlineKeyboardMarkup()
        buttonA = telebot.types.InlineKeyboardButton('Человек', callback_data='Человек')
        buttonB = telebot.types.InlineKeyboardButton('Дварф', callback_data='Дварф')
        buttonC = telebot.types.InlineKeyboardButton('Эльф', callback_data='Эльф')
        buttonD = telebot.types.InlineKeyboardButton('Гном', callback_data='Гном')
        buttonE = telebot.types.InlineKeyboardButton('Полурослик', callback_data='Полурослик')
        buttonF = telebot.types.InlineKeyboardButton('Полуорк', callback_data='Полуорк')
        buttonG = telebot.types.InlineKeyboardButton('Полуэльф', callback_data='Полуэльф')
        buttonH = telebot.types.InlineKeyboardButton('Драконорождённый', callback_data='Драконорождённый')
        buttonI = telebot.types.InlineKeyboardButton('Тифлинг', callback_data='Тифлинг')

        markup.row(buttonA, buttonB, buttonC, buttonD)
        markup.row(buttonE, buttonF, buttonG, buttonI)
        markup.row(buttonG, buttonH)

        bot.send_message(message.chat.id, 'Выбери расу, прочти про неё и реши, подходит ли она для тебя',
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.data == 'start':
        print()
    elif call.data == 'stop':
        print()
    elif call.data == 'upload':
        print()
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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите'
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



######


bot.polling()
