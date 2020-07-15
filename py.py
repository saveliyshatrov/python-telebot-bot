import telebot
import time
import random
import json

bot = telebot.TeleBot('1132412619:AAFk-IMvCm3aZsf-sS_Q4etm3Hcz-f0_E-A')


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


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=Main_Keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Быстрое решение':
        bot.send_message(message.chat.id, 'Выбери тариф', reply_markup = Fast_decision)

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


bot.polling(none_stop=True)
