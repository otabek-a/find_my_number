from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
from tinydb import TinyDB, Query
from begin import start
from my_num import find_number, find
from number_bot import find_bot, bot_find
from result import result_bot, clear_data
from change_num import change,change_son,res
from config import TOKEN




def son_num():
    number=res
    return number


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def main():
   dispatcher.add_handler(MessageHandler(Filters.regex(r'\bfrom\b'), change_son))
   dispatcher.add_handler(MessageHandler(Filters.text('Change range of numbers'),change))
   dispatcher.add_handler(MessageHandler(Filters.text('🗑️ Clear History 🔄'), clear_data))
   dispatcher.add_handler(MessageHandler(Filters.text('📊 View Results 📜'), result_bot))
   dispatcher.add_handler(MessageHandler(Filters.text('🤖 Find number of robot 🎲'), find_bot))
   dispatcher.add_handler(MessageHandler(Filters.text('➕ Increase 🔼'), find))
   dispatcher.add_handler(MessageHandler(Filters.text('➖ Decrease 🔽'), find))
   dispatcher.add_handler(MessageHandler(Filters.text('✅ Correct! 🎯'), find))
   dispatcher.add_handler(MessageHandler(Filters.text("🎮 Let's play bro 🎲"), find))
   dispatcher.add_handler(CommandHandler('start', start))
   dispatcher.add_handler(MessageHandler(Filters.text('🔙 Back to main menu'), start))
   dispatcher.add_handler(MessageHandler(Filters.text('🔢 Find my number 🔍'), find_number))
   dispatcher.add_handler(MessageHandler(Filters.regex(r'^\d+$'), bot_find))
 


if __name__=='__main__':
    main()
updater.start_polling()
updater.idle()
