import telebot
from valuables import telegramApi
bot = telebot.TeleBot(telegramApi)

#todo

bot.polling(none_stop=True, interval=0)
