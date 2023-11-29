import telebot

bot = telebot.TeleBot('6695142409:AAHY15bhMIqqyFE9ymbkQ7cKTTfztZecM5Q')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')

@bot.message_handler(commands=['jump'])
def main(message):
    bot.send_message(message.chat.id, 'ПРЫГАЙ!!! \nПРЫГАЙ!!!')


bot.infinity_polling()