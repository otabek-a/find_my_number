from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from config import TOKEN
import random
bot=TinyDB('result.json')
a = 1
b = 10
count = 0
son = random.randint(a, b)

def find_bot(update: Update, context):
    update.message.reply_text(f"🤖 Welcome! Please find my number 🔢🎯⬇️ from {a} to {b}")

def bot_find(update, context):
    global a, b, count, son
 
    text = update.message.text
    text = int(text)

    if son < text:
        count += 1
        update.message.reply_text("📉 My number is **smaller** than your number! Try again 🔄")

    elif son > text:
        count += 1
        update.message.reply_text("📈 My number is **greater** than your number! Keep going! 🎯")

    elif son == text:
        count += 1
        bot.insert({'you':count})
        update.message.reply_text(f"🎉 You found my number in {count} tries! 🏆🎊")

    else:
        update.message.reply_text("⚠️ Something went wrong! Please start again by sending /start. 🔄")
