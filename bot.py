import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_API_TOKEN' with the token you obtained from BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Function to handle the '/start' command
def start(update: Update, _: CallbackContext):
    update.message.reply_text("Hello! I can run commands on your computer. Send /help to see the list of available commands.")

# Function to handle the '/help' command
def help_command(update: Update, _: CallbackContext):
    update.message.reply_text("Available commands:\n /run <command> - Run a command on your computer.")

# Function to handle the '/run' command
def run_command(update: Update, _: CallbackContext):
    user_command = update.message.text[len('/run '):]
    result = subprocess.getoutput(user_command)
    update.message.reply_text(result)

def main():
    updater = Updater(API_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("run", run_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
