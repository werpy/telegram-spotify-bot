# - *- coding: utf- 8 - *-
import telebot
import spotify
from decouple import config as env_conf

token = env_conf('TELEGRAM_BOT_TOKEN', cast=str)

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправь мне название песни, а я найду тебе саму песню")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    print(message.text)
    bot.reply_to(message, spotify.get_track(message.text))


bot.polling()
