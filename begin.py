from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from config import TOKEN

def start(update: Update, context):
    reply = [
        ['🔢 Find my number 🔍', '🤖 Find number of robot 🎲'],
        ['📊 View Results 📜', '🗑️ Clear History 🔄']
    ]
    key = ReplyKeyboardMarkup(reply, resize_keyboard=True)

    update.message.reply_text(
        "👋 *Hello, dear player!* 🎮 Welcome to the **Random Numbers Bot** 🤖!\n\n"
        "🎯 Choose an option below to start playing: ⬇️\n\n"
        "🔢 *Find My Number* - I will guess your number!\n"
        "🤖 *Find Number of Robot* - Try to guess my secret number!\n"
        "📊 *View Results* - Check your previous attempts!\n"
        "🗑️ *Clear History* - Reset all data and start fresh! 🔄",
        parse_mode="Markdown",
        reply_markup=key
    )
