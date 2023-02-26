import telebot
import random as r
from telebot import types
import time
import sqlite3
import os, subprocess

#-- Мои библиотеки--
from detals import cpicok

bot = telebot.TeleBot('----')
'''
 Список всех пользователей
 Счет деталей
 Задачи коптер коины
 Авторизация
'''

conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   username TEXT,
   fname TEXT,
   grupa TEXT,
   age INT,
   Competence TEXT,
   Coptercoin INT,
   last_action TEXT,
   admin int);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Detals(
   id INT PRIMARY KEY,
   Detals TEXT,
   quantity INT,
   total TEXT);
""")

print("Бот запущен!")
file = open('detals.txt','r')
bank_file = open('bank.txt','r')
CopterCoin = 0
kvest = 0

def Rewriting(Action):
    user = (message.id, message.from_user.username, message, "-", "-", 0, "-", 0, "regestration", 1 )
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
    conn.commit()

@bot.message_handler(commands=['start']) #Первое сообщение при запуске бота
def start(message):
    # Добавление кнопки прикрепленной к сообщению
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Мой телеграмм", url='https://t.me/RATTER0')
    markup.add(button1)
    #Добавление кнопок
    markup_Inside = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🌎 Регистрация")
    btn2 = types.KeyboardButton("🌦️ Погода")
    btn3 = types.KeyboardButton("📰 Новости")
    markup_Inside.add(btn1,btn2,btn3)
    #Отправка сообщений
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Если увидишь какие либо баги, то срочно сообщи мне о них!)".format(message.from_user), reply_markup=markup)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHzyRj8kDdda2LbXTlXF-yl-FAgEPMTwACvxYAAs1FuEreBBj0UDUS7y4E')
    bot.send_message(message.chat.id, "С чего начнем?", reply_markup=markup_Inside)

    user = (message.id, message.from_user.username, "-", "-", "-", 0, "-", 0, "start bot", 0 )
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
    conn.commit()

@bot.message_handler(commands=['secret','list','/lider_board, /balance'])
def comands(message):
     if message.text == '/secret':
         bot.send_message(message.chat.id, 'Секрет успешно активирован')
         img = 'https://yandex.ru/images/search?text=%20%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5&from=tabbar&pos='+str(r.randint(1,1000))+'&img_url=https%3A%2F%2Fget.wallhere.com%2Fphoto%2Fillustration-blonde-long-hair-anime-anime-girls-lookin'
         bot.send_photo(message.chat.id, photo=img)

     if message.text == '/list':
        with open('detals.txt') as file:
            while (line := file.readline().rstrip()):
                bot.send_message(message.chat.id, line)

     if message.text == '/lider_board':
        with open('ban.txt') as file:
            while (line := file.readline().rstrip()):
                bot.send_message(message.chat.id, line)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global kvest,CopterCoin,i,step
    if message.text == "🌎 Регистрация":
        name = str(message.from_user.first_name)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Поехали!", callback_data='Step_1')
        markup.add(button1)
        bot.reply_to(message, "Хорошо для того что бы зарегестроваться нужно немного рассказать о себе.", reply_markup=markup)
        step = 1
        bot.send_message(message.from_user.id,  "Отлично!" + name + "\n Добро пожаловать в нашу команду)")

    elif (message.text == "📑 Подсчет деталей") and (kvest == 0):
        bot.send_message(message.from_user.id, 'Хорошо пиши название детали и их количество \n Например "Ключ для пропеллеров 5" Напиши Стоп, когда закончишь подсчет')
        markup_Inside = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Список всех деталей")
        markup_Inside.add(btn1)
        CopterCoin += 10
        kvest = 1

    elif (message.text == "Стоп") and (kvest == 1):
        bot.send_message(message.from_user.id, "Молодец! Твои труды не будут безвозмездны. Вот тебе " + str(CopterCoin) + " коптеркоинов")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHuRxj6jZgWzfsg8kXz2uPYU5JXD3hvwACOBkAAntfQEmO99QKq9iyTC4E')
        cpicok.writeBank(message.from_user.first_name,CopterCoin)
        kvest = 0

    elif kvest == 1:
        detal = []
        cpicok.search(message.text,detal)
        markup = types.InlineKeyboardMarkup(row_width=1)
        for i in detal:
            count = 1
            item = types.InlineKeyboardButton(i, callback_data = i)
            markup.add(item)
        button1 = types.InlineKeyboardButton("Список всех деталей", callback_data='All')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Возможно вы имели ввиду:', reply_markup=markup)


    if (message.text == "Список всех деталей") and (kvest == 1):
        bot.send_message(message.from_user.id, 'Хорошо пиши название детали и их количество \n Например "Ключ для пропеллеров 5" Напиши Стоп, когда закончишь подсчет')
        CopterCoin += 10
        kvest = 1

    elif message.text == "Дай квест":
        bot.send_message(message.from_user.id, "Напиши привет")

    elif step == 1:
        cur.execute("DELETE FROM users WHERE userid='" + message.id + "';")
        user = (message.id, message.from_user.username, message, "-", "-", 0, "-", 0, "regestration", 1 )
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?);", user)
        step = 2



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    global i
    if call.message:
        if call.data == 'All':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Список всех деталей:')
            # Скинуть фото
        elif call.data == i:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= i)
        elif call.data == "Step_1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Для начала напиши своё ФИО")

bot.polling()
