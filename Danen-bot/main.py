import telebot

token = ""

bot = telebot.TeleBot(token)


string = ["Darya", "darya", "Дарья", "дарья"]


@bot.message_handler(content_types=["text"])
def echo(message):
    name = message.text
    if name in string:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, "Брысь, я тебя не знаю!")


bot.polling(none_stop=True)
