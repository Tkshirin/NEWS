import telebot
from MyToken import token
from telebot import types
from main import main
import csv

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,main())

bot.polling()