from datetime import date

import telebot
from telebot import types

from get_daily_tasks import get_daily_tasks
from secrets import token

bot = telebot.TeleBot(token)

subjects = ['lectura', 'matemáticas', 'cc naturales', 'cc sociales',
            'educación física', 'lengua', 'inglés', 'tecnología', 'música', 'plástica']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    start_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    start_markup.row('/tareas', '/ayuda', '/ocultar')
    bot.send_message(message.from_user.id,
                     '''¡¡Hola!! Dale a /ayuda para ver cómo funciona el bot.\
                    Puedes ocultar las opciones con /ocultar.\
                    \nMuestra de nuevo las opciones escribiendo /start.''',
                     reply_markup=start_markup)


@bot.message_handler(commands=['ocultar'])
def hide_command(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'ocultamos teclado',
                     reply_markup=hide_markup)


@bot.message_handler(commands=['tareas'])
def show_tasks(message):
    daily_tasks = get_daily_tasks()
    bot.send_message(
        message.chat.id, 'Hoy tenemos que trabajar estas asignaturas:')
    for x in daily_tasks:
        bot.send_message(message.chat.id, x)
    bot.send_message(
        message.chat.id, '¿Con cuál quieres comenzar?')


@bot.message_handler(commands=subjects)
pass
# function that uploads work sheets
# function that uploads audio file
# function that asks for sums or substractions
# function that tells the exersices in English
bot.polling()
# https://github.com/irevenko/info-bot/blob/master/bot.py
