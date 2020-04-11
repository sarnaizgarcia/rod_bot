from datetime import date

import telebot
from telebot import types

from tasks_manager import get_daily_tasks, get_task_data
from planning import homework_planning
from secrets import token

bot = telebot.TeleBot(token)

subjects = ['lectura', 'matemáticas', 'naturales', 'sociales',
            'educación física', 'lenguaje', 'inglés', 'tecnología', 'música', 'plástica']


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
def select_subject(message):
    daily_tasks = get_daily_tasks()  # gets a list with the subjects
    bot.send_message(
        message.chat.id, 'Hoy tenemos que trabajar estas asignaturas:')  # sends the list of subjects
    for x in daily_tasks:
        bot.send_message(message.chat.id, x)
    subject_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    for subject in daily_tasks:
        subject_markup.row(f'/{subject}')
    subject_markup.row('/ocultar')
    bot.send_message(
        message.chat.id, '''¿Con cuál quieres comenzar?\
        \nRecuerda que puedes ocultar las opciones con /ocultar.''',
        reply_markup=subject_markup)


@bot.message_handler(commands=subjects)
def get_tasks_detail(message):
    # once a subject has been chosen, gives the details of the task
    subject_slash = message.text
    subject = subject_slash[1:]
    task_title = get_task_data('title', subject)
    task_description = get_task_data('description', subject)
    task_source = get_task_data('source', subject)
    # chek what type of task is required for the subjet
    bot.send_message(message.chat.id, subject.upper())
    bot.send_message(message.chat.id, task_title)
    bot.send_message(message.chat.id, task_description)
    bot.send_message(message.chat.id, task_source)
    finish_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    finish_markup.add('/terminar')
    msg = bot.send_message(
        message.chat.id, 'Si has terminado elige /terminar', reply_markup=finish_markup)
    bot.register_next_step_handler(msg, finish_task)


@bot.message_handler(commands=['terminar'])
def finish_task(message):
    pass


# function that uploads work sheets
# function that uploads audio file
# function that asks for sums or substractions
# function that tells the exersices in English
bot.polling()
# https://github.com/irevenko/info-bot/blob/master/bot.py
