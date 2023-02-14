import telebot
import random as r
from telebot import types
import time
import os, subprocess
#-- Мои библиотеки--
from detals import cpicok

bot = telebot.TeleBot('---------------------')
print("Бот запущен!")
file = open('detals.txt','r')
bank_file = open('bank.txt','r')
CopterCoin = 0
kvest = 0
@bot.message_handler(commands=['help','secret','list','/lider_board, /balance'])
def comands(message):
     if message.text == '/help':
         bot.send_message(message.chat.id, '/secret - секрет \n /list - список всех деталей')

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
    global kvest,CopterCoin
    if (message.text == "Подсчет деталей") and (kvest == 0):
        bot.send_message(message.from_user.id, 'Хорошо пиши название детали и их количество \n Например "Ключ для пропеллеров 5" Напиши Стоп, когда закончишь подсчет')
        CopterCoin += 10
        kvest = 1

    elif (message.text == "Стоп") and (kvest == 1):
        bot.send_message(message.from_user.id, "Молодец! Твои труды не будут безвозмездны. Вот тебе " + str(CopterCoin) + " коптеркоинов")
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHuRxj6jZgWzfsg8kXz2uPYU5JXD3hvwACOBkAAntfQEmO99QKq9iyTC4E')
        cpicok.writeBank(message.from_user.first_name,CopterCoin)
        kvest = 0

    elif kvest == 1:
        bot.send_message(message.from_user.id, cpicok.search(message.text))
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("❓ Задать вопрос")

    elif message.text == "Регистрация":
        name = str(message.from_user.first_name)
        bot.reply_to(message, "Привет!" + name + "\n Добро пожаловать в нашу команду)")
        bot.send_message(message.from_user.id, "Напиши привет")

    elif message.text == "Дай квест":
        bot.send_message(message.from_user.id, "Напиши привет")

bot.polling()
