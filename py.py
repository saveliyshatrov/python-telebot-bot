#1132412619:AAFk-IMvCm3aZsf-sS_Q4etm3Hcz-f0_E-A
import telebot
from telebot import apihelper
import time


"""ip = '145.239.81.69'
port = '1080'

apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip,port)
}"""

print(apihelper.proxy)

bot = telebot.TeleBot('1132412619:AAFk-IMvCm3aZsf-sS_Q4etm3Hcz-f0_E-A')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Что за время?')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Что за время?':
        bot.send_message(message.chat.id, str(time.ctime()))
    else:
        print(message.text)
        bot.send_message(message.chat.id, 'Ybxtuj yt gjyzk, yj jxtym bynthtcyj')
    print(time.ctime())

bot.polling(none_stop=True)