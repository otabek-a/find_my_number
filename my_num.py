from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from config import TOKEN
import random
bot=TinyDB('result.json')
a=1
b=10
count=0
son=0
def find_number(update: Update, context):
    reply = [
          ["🎮 Let's play bro 🎲"],
        ['➕ Increase 🔼', '➖ Decrease 🔽'],
        ['✅ Correct! 🎯'],
        ['🔙 Back to main menu']
    ]
    key = ReplyKeyboardMarkup(reply, resize_keyboard=True)
    

    update.message.reply_text("🤖 Welcome! Please help me find your number using the buttons below ⬇️",reply_markup=key)

def find(update,context):
    global a,b,count,son
 
    
    matn=update.message.text
    
    if matn=='➕ Increase 🔼':
            a=son+1
            count+=1
           
           

    elif matn=='➖ Decrease 🔽':
            b=son-1
            count+=1
            
            
    elif matn=='✅ Correct! 🎯':
            count+=1
            bot.insert({'bot':count})
            update.message.reply_text(f"🎉 I found your number in {count} tries! 🏆")
            a, b = 1, 10
            count = 0
            son = random.randint(a, b)
            return

    if a <= b:
        son = random.randint(a, b)
        update.message.reply_text(f"🤔 Is your number {son}? 🔢")
    else:
        a, b = 1, 10
        count = 0
        son = random.randint(a, b)
        update.message.reply_text("⚠️ Something went wrong! Please start again by sending /start. 🔄")
