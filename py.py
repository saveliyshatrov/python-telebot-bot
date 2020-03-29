import telebot
"""from telebot import apihelper"""
import time
import random

# oleg_ne_oleg_no_oleg

"""ip = '145.239.81.69'
port = '1080'
apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip,port)
}"""

"""print(apihelper.proxy)"""

bot = telebot.TeleBot('your token here')

Main_Keyboard = telebot.types.ReplyKeyboardMarkup()
fast_buy = telebot.types.KeyboardButton('Быстрое решение')
about_tarifs = telebot.types.KeyboardButton('Тарифы')
about_us = telebot.types.KeyboardButton('О нас')
_help = telebot.types.KeyboardButton('Help')
close = telebot.types.KeyboardButton('Закрыть')
Main_Keyboard.add(fast_buy)
Main_Keyboard.add(about_tarifs)
Main_Keyboard.add(about_us, _help)
Main_Keyboard.add(close)

Tarifs = telebot.types.ReplyKeyboardMarkup()
Tarif_1 = telebot.types.KeyboardButton('Тариф 1')
Tarif_2 = telebot.types.KeyboardButton('Тариф 2')
Tarif_3 = telebot.types.KeyboardButton('Тариф 3')
quit_to_main_menu = telebot.types.KeyboardButton('В главное меню')
Tarifs.add(Tarif_1)
Tarifs.add(Tarif_2)
Tarifs.add(Tarif_3)
Tarifs.add(quit_to_main_menu)

Fast_decision = telebot.types.ReplyKeyboardMarkup()
Physic = telebot.types.KeyboardButton('Физика')
Coming_soon = telebot.types.KeyboardButton('Будет скоро')
soon = telebot.types.KeyboardButton('Будет скоро')
Fast_decision.add(Physic)
Fast_decision.add(Coming_soon)
Fast_decision.add(Coming_soon)
Fast_decision.add(quit_to_main_menu)

Help = telebot.types.ReplyKeyboardMarkup()
Question_1 = telebot.types.KeyboardButton('Популярный вопрос 1')
Question_2 = telebot.types.KeyboardButton('Популярный вопрос 2')
Question_3 = telebot.types.KeyboardButton('Популярный вопрос 3')
Help.add(Physic)
Help.add(Coming_soon)
Help.add(Coming_soon)
Help.add(quit_to_main_menu)


OWNER_ID = 133907668
ANN_ID = 287201315
ARTUR_ID = 617071251


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, ты написал мне /start', reply_markup=Main_Keyboard)  # keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Быстрое решение':
        bot.send_message(OWNER_ID, 'Хотят купить подписку')
        random_number = str(random.randrange(10,30, 1)/10)
        bot.send_message(message.chat.id, 'Выбери тариф и коеффицент цены сейчас x' + str(random_number),
                         reply_markup=Fast_decision)

    elif message.text == 'Тарифы':
        bot.send_message(message.chat.id, 'Тарифы', reply_markup=Tarifs)

    elif message.text == 'О нас':
        bot.send_message(message.chat.id, 'О нас', reply_markup=Main_Keyboard)
        #bot.send_message(ANN_ID, str(message.chat.id), reply_markup=markup)

    elif message.text == 'Help':
        bot.send_message(message.chat.id, 'Help', reply_markup=Main_Keyboard)

    elif message.text == 'Закрыть':
        bot.send_message(message.chat.id, 'Закрыть')

    elif message.text == 'В главное меню':
        bot.send_message(message.chat.id, '<----', reply_markup=Main_Keyboard)

    else:
        print(message.text)
        bot.send_message(message.chat.id, str(time.ctime()))
    print(time.ctime())


bot.polling(none_stop=True)
