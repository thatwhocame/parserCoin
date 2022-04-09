import telebot
import logging
from valuables import *

bot = telebot.TeleBot(telegramApi)


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.from_user.id, start_mess)


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.from_user.id, help_mess)


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=.5)

bot.polling(none_stop=True)

if __name__ == '__main__':
    main(True, 'DEBUG')
