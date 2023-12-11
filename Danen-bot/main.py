from random import choice

import telebot

token = ""

bot = telebot.TeleBot(token)


RANDOM_TASKS = [
    "Написать Гвидо письмо",
    "Выучить звездную карту",
    "Отправить Миленькой смайлик",
    "Посмотреть 4 сезон Боевого континента",
]

todos = {}


HELP = """
Список доступных команд:
* /add + день + текст задачи- несколько задач, можно добавить через запятую 
* /random - добавить на сегодня случайную задачу
* /show + день - напечать все задачи на заданный день
"""


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет, я Тикса, твой помощник с записью важных дел. Чтобы начать работу, введи: /ok"
    )


def add_todo(day, task):
    day = day.lower()
    if todos.get(day) is not None:
        todos[day].append(task)
    else:
        todos[day] = [task]


@bot.message_handler(commands=["ok"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["random"])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo("сегодня", task)
    bot.send_message(message.chat.id, f"Задача {task} добавлена на сегодня")


@bot.message_handler(commands=["add"])
def add(message):
    _, day, tail = message.text.split(maxsplit=2)
    day = day.lower()

    tasks = tail.split(",")

    for task in tasks:
        task = task.strip()
        add_todo(day, task)

    bot.send_message(message.chat.id, f"{len(tasks)} задачи добавлены на {day}")


@bot.message_handler(commands=["show"])
def show(message):
    _, day = message.text.split(maxsplit=2)
    day = day.lower()

    if day in todos:
        tasks = todos[day]

        if len(tasks) > 0:
            task_list = "\n".join(tasks)
            bot.send_message(message.chat.id, f"Задачи на {day}:\n{task_list}")
        else:
            bot.send_message(message.chat.id, f"На {day} нет задач")
    else:
        bot.send_message(message.chat.id, "Такого дня нет")


bot.polling(none_stop=True)
