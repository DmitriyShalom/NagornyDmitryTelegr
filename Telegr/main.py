import telebot
from telebot import types
import psycopg2
import datetime

bot = telebot.TeleBot('2104138555:AAEwwr13MBf_g4UnI6HXiLJEmEjMhifRgKQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_help = types.KeyboardButton('/help')
    btn_timetable = types.KeyboardButton('Расписание')
    markup.row(btn_help)
    markup.row(btn_timetable)
    bot.send_message(message.chat.id, 'Привет\n/help', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Команды:\n/start - начало пользования ботом.\n/help - помощь.'
                     '\nРасписание - показать расписание.')


@bot.message_handler(commands=['back'])
def back_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_help = types.KeyboardButton('/help')
    btn_timetable = types.KeyboardButton('Расписание')
    markup.row(btn_help)
    markup.row(btn_timetable)
    bot.send_message(message.chat.id, 'Главное меню\n/help', reply_markup=markup)


@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_yst = types.KeyboardButton('Вчера')
        btn_tdy = types.KeyboardButton('Сегодня')
        btn_tmr = types.KeyboardButton('Завтра')
        btn_wik = types.KeyboardButton('День недели')
        btn_back = types.KeyboardButton('/back')
        markup.row(btn_yst, btn_tdy, btn_tmr)
        markup.row(btn_wik)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Какой день?', reply_markup=markup)
    if message.text == 'Вчера':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        week = ["'Понедельник'", "'Вторник'", "'Среда'", "'Четверг'", "'Пятница'"]
        wd = datetime.datetime.today().weekday() - 1
        if wd > 4 or wd == -1:
            wd = 4
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day=" + week[wd])
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Сегодня':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        week = ["'Понедельник'", "'Вторник'", "'Среда'", "'Четверг'", "'Пятница'"]
        wd = datetime.datetime.today().weekday()
        if wd > 4:
            wd = 1
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day=" + week[wd])
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Завтра':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        week = ["'Понедельник'", "'Вторник'", "'Среда'", "'Четверг'", "'Пятница'"]
        wd = datetime.datetime.today().weekday() + 1
        if wd > 4 or wd == 7:
            wd = 1
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day=" + week[wd])
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'День недели вручную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_mon = types.KeyboardButton('Понедельник')
        btn_tue = types.KeyboardButton('Вторник')
        btn_wed = types.KeyboardButton('Среда')
        btn_thu = types.KeyboardButton('Четверг')
        btn_fri = types.KeyboardButton('Пятница')
        btn_all = types.KeyboardButton('Вся неделя')
        markup.row(btn_all)
        markup.row(btn_mon, btn_tue, btn_wed)
        markup.row(btn_thu, btn_fri)
        bot.send_message(message.chat.id, 'Какой день недели?', reply_markup=markup)
    if message.text == 'Понедельник':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day='Понедельник';")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Вторник':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day='Вторник';")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Среда':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day='Среда';")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Четверг':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day='Четверг';")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Пятница':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT pos, subject, room, start FROM timetable WHERE day='Пятница';")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()
    if message.text == 'Вся неделя':
        conn = psycopg2.connect(database="tabledb",
                                user="postgres",
                                password="1234",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT day, pos, subject, room, start FROM timetable")
        row = list(cursor.fetchall())
        mess = ''
        for i in row:
            mess += '(' + str(i[0]) + ') '
            mess += str(i[1]) + ' '
            mess += str(i[2]) + ' '
            mess += str(i[3]) + '\n'
        bot.send_message(message.chat.id, mess)
        conn.close()


bot.infinity_polling()
