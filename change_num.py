from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from begin import start
from my_num import find_number, find
from number_bot import find_bot, bot_find
from result import result_bot, clear_data
import random
from config import TOKEN
res=[1,10]
def change(update,context):
    update.message.reply_text('Please if you change range of numbers please send your numbers after from, example: from 1-10 ')
def change_son(update,context):
    global res, a, b, son
    matn = update.message.text
    matn = matn.replace('from', '').strip()
    matn = matn.split('-')
    
    if len(matn) == 2 and matn[0].isdigit() and matn[1].isdigit():
        a, b = int(matn[0]), int(matn[1])
        res = [a, b]
        son = random.randint(a, b) 
        update.message.reply_text(f'✅ You changed the range from {a} to {b}')
    else:
        update.message.reply_text('⚠️ Sorry, you entered the wrong format. Please use: from 1-10')
