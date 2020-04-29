import telebot
"""from telebot import apihelper"""
import time
import random
import json

bot = telebot.TeleBot('YOUR_TOKEN_HERE')


def CreateKeyboard(ArrayOfButtons):
    keyboard = json.dumps({"keyboard": ArrayOfButtons})
    return keyboard


Main_Keyboard = CreateKeyboard([
    ['Быстрое решение'],
    ['Тарифы'],
    ['О нас', 'Help'],
    ['Закрыть']
])

Tarifs = CreateKeyboard([
    ['Тариф 1'],
    ['Тариф 2'],
    ['Тариф 3'],
    ['В главное меню']
])

Fast_decision = CreateKeyboard([
    ['Физика'],
    ['Будет скоро'],
    ['Будет скоро'],
    ['В главное меню']
])

Help = CreateKeyboard([
    ['Популярный вопрос 1'],
    ['Популярный вопрос 2'],
    ['Популярный вопрос 3'],
    ['В главное меню']
])

MY_ID = 133907668
ANN_ID = 287201315
ARTUR_ID = 617071251


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=Main_Keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Быстрое решение':
        bot.send_message(MY_ID, 'Хотят купить подписку')
        random_number = str(random.randrange(10, 30, 1)/10)
        bot.send_message(message.chat.id, 'Выбери тариф и коеффицент цены сейчас x' + str(random_number), reply_markup = Fast_decision)

    elif message.text == 'Тарифы':
        bot.send_message(message.chat.id, 'Тарифы', reply_markup = Tarifs)

    elif message.text == 'О нас':
        bot.send_message(message.chat.id, 'О нас', reply_markup = Main_Keyboard)

    elif message.text == 'Help':
        bot.send_message(message.chat.id, 'Help', reply_markup = Main_Keyboard)

    elif message.text == 'Закрыть':
        bot.send_message(message.chat.id, 'Пока пока(((')

    elif message.text == 'В главное меню':
        bot.send_message(message.chat.id, '⬅', reply_markup = Main_Keyboard)

    else:
        print(message.text)
        bot.send_message(ANN_ID, message.text)


bot.polling(none_stop=True)
