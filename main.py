import telebot
import logging
from valuables import *
from db.db import db_table_val

bot = telebot.TeleBot(telegramApi)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.from_user.id, start_mess)


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.from_user.id, help_mess)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'вход':
        us_id = message.from_user.id
        us_name = bot.send_message(message.chat.id, 'Напиши свое имя')
        us_pref = bot.send_message(message.chat.id, 'Напиши про крипту').text
        bot.register_next_step_handler(us_pref, db_table_val(us_id, str(us_name), str(us_pref)))


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=.5)


bot.polling(none_stop=True)

if __name__ == '__main__':
    main(True, 'DEBUG')
