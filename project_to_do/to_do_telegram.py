import time

import telebot
from telebot import types

TOKEN = "857373928:AAFnABpe7nXYLZ2WvNBr4hv4ryT4MVgM9y0"

bot = telebot.TeleBot(TOKEN)

COMMANDS = {
    'list'        : 'Current tasks',
    'done'        : 'Finish task with number #',
    'all'         : 'All tasks',
    'completed'   : 'Show all finished tasks',
    'feedback'    : 'Write us feedback',
    'add'         : 'Add task'
    }
tasks = []

@bot.message_handler(commands=['help'])
def command_help(message):
    id = message.chat.id
    help_text = "The following commands are available: \n"
    for key in COMMANDS:
        help_text += "/" + key + ": "
        help_text += COMMANDS[key] + "\n"
    bot.send_message(id, help_text)

@bot.message_handler(commands=['add'])
def command_image(message):
    id = message.chat.id
    bot.send_message(id, "Please enter your task")

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def command_default(message):
        tasks.append(message.text)
        bot.send_message(message.chat.id, "Task added")

@bot.message_handler(commands=['all'])
def command_image(message):
    id = message.chat.id
    bot.send_message(id, str(tasks[0]))


if __name__ == "__main__":
    bot.polling(none_stop=True)