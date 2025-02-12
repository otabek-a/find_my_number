from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from begin import start
from my_num import find_number, find
from number_bot import find_bot ,bot_find
from config import TOKEN
bot=TinyDB('result.json')
def result_bot(update, context):
    matn = bot.all()  
    
    if matn:
        text = "📊 *User Results:* 📊\n\n"  
        for index, item in enumerate(matn, start=1): 
            text += f"🔹 *User {index}:*\n"
            for key, value in item.items(): 
                text += f"   🔸 *{key.capitalize()}* ➝ `{value}`\n"
            text += "➖➖➖➖➖➖➖➖➖➖\n" 
        update.message.reply_text(text, parse_mode="Markdown")  
    else:
        update.message.reply_text("⚠️ *Database is empty!* ❌", parse_mode="Markdown")
def clear_data(update, context):
    bot.truncate() 
    update.message.reply_text("🗑️ *All data has been cleared!* ✅", parse_mode="Markdown")
