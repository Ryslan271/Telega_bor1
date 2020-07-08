from models.start import bot
from models.users import lalala


@bot.message_handler(commands=['start'])
def welcome(message):
    lalala1(message)


@bot.message_handler(content_types=['text'])
def lalala1(message):
    lalala(message)


bot.polling(none_stop=True)
