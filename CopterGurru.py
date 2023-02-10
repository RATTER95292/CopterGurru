import telebot
import random as r
import time
#-- Мои библиотеки--
from detals import cpicok

bot = telebot.TeleBot('---')
print("Бот запущен!")
file = open('detals.txt','r')
@bot.message_handler(commands=['help','secret','list'])
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
bot.polling()
