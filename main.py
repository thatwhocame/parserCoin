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
        global us_id
        us_id = message.from_user.id
        bot.send_message(message.chat.id, 'Напиши свое имя')
        bot.register_next_step_handler(message, prefs)

def prefs(message):
    global us_name
    us_name = message.text
    bot.send_message(message.chat.id, 'Напиши про крипту')
    bot.register_next_step_handler(message, upd)

def upd(message):
    us_pref = message.text
    db_table_val(us_id, us_name, us_pref)
    bot.send_message(message.chat.id, f'Вход выполнен! Проверь правильность введенных данных:\nИмя: {us_name}\nОтслеживаемые монеты: {us_pref}')


def main(use_logging, level_name):
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))
    bot.polling(none_stop=True, interval=.5)


bot.polling(none_stop=True)

if __name__ == '__main__':
    main(True, 'DEBUG')
