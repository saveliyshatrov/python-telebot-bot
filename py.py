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

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    print(time.ctime())

bot.polling(none_stop=True)