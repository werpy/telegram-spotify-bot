import telebot
import spotify

bot = telebot.TeleBot('1718861283:AAEakPdTr-84BL304y-zXhX7mXCu6KoalfY')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправь мне название песни, а я найду тебе саму песню")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, spotify.get_track(message.text))


bot.polling()
