from datetime import date

import telebot
from telebot import types

from tasks_manager import (get_daily_tasks,
                           get_task_data,
                           remove_subject,
                           modify_task_state)
from planning import homework_planning
from secrets import token
from controllers.user_creation import user_creation

bot = telebot.TeleBot(token)

subjects = ['lectura', 'matemáticas', 'naturales', 'sociales',
            'educación física', 'lenguaje', 'inglés', 'tecnología', 'música', 'plástica']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(f'{type(message.from_user.id)} - {type(message.from_user.first_name)}')
    print(f'{message.from_user.id} - {message.from_user.first_name}')
    # user_id = message.from_user.id
    # user_name = message.from_user.first_name
    user = user_creation(1, 'Pepe')
    print(user)
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
        message.from_user.id, 'Hoy tenemos que trabajar estas asignaturas:')  # sends the list of subjects
    for x in daily_tasks:
        bot.send_message(message.from_user.id, x)
    subject_markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    for subject in daily_tasks:
        subject_markup.row(f'/{subject}')
    subject_markup.row('/ocultar')
    bot.send_message(
        message.from_user.id, '''¿Cuál quieres hacer?\
        \nRecuerda que puedes ocultar las opciones con /ocultar.''',
        reply_markup=subject_markup)


@bot.message_handler(commands=subjects)
def get_tasks_detail(message):
    # once a subject has been chosen, gives the details of the task
    subject_slash = message.text
    global subject
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
        message.from_user.id, '''Si has terminado, pulsa /terminar.\
            \nPara ver de nuevo todas las tareas pendientes de hoy, /tareas.''',
        reply_markup=finish_markup)
    # bot.register_next_step_handler(msg, finish_task)


@bot.message_handler(commands=['terminar'])
def finish_task(message):  # Por aquí tiene que pasar la asignatura
    daily_tasks = get_daily_tasks()
    updated_task_state = modify_task_state(subject)
    updated_daily_tasks = remove_subject(daily_tasks, subject)
    if len(daily_tasks) > 0:
        bot.send_message(
            message.from_user.id, 'Para continuar con las demás tareas /tareas')
    if len(daily_tasks) == 0:
        bot.send_message(
            message.from_user.id, 'Has terminado por hoy ¡Buen trabajo!')


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling()
# https://github.com/irevenko/info-bot/blob/master/bot.py
