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
                     '''¡¡Hola!! Elije /ayuda para ver cómo funciona el bot.\
                    Puedes ocultar las opciones con /ocultar.\
                    \nMuestra de nuevo las opciones escribiendo /start.\
                    \nSi quieres ver los deberes de hoy elige /tareas''',
                     reply_markup=start_markup)


@bot.message_handler(commands=['ocultar'])
def hide_command(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'ocultamos teclado',
                     reply_markup=hide_markup)


@bot.message_handler(commands=['tareas'])
def show_tasks(message):
    daily_tasks = get_daily_tasks()
    bot.send_message(
        message.chat.id, 'Hoy tenemos que trabajar estas asignaturas:')
    for x in daily_tasks:
        bot.send_message(message.chat.id, x)
    start_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    for subject in daily_tasks:
        start_markup.row(f'/{subject}')
    start_markup.row('/ocultar')
    bot.send_message(
        message.chat.id, '''¿Con cuál quieres comenzar?\
        \nRecuerda que puedes ocultar las opciones con /ocultar.''',
        reply_markup=start_markup)


# @bot.message_handler(commands=['subjects'])
# def choose_task(message):
#     start_markup = telebot.types.ReplyKeyboardMarkup(
#         resize_keyboard=True, one_time_keyboard=False)
#     for _ in subjects:
#         start_markup.row(_)


# function that uploads work sheets
# function that uploads audio file
# function that asks for sums or substractions
# function that tells the exersices in English
bot.polling()
# https://github.com/irevenko/info-bot/blob/master/bot.py
