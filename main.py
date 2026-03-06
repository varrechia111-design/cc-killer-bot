from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Function to register a user


def register(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('You have been registered!')

# Function to delete a user

def delete(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('You have been deleted!')

# Function to list users

def list_users(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Listing users...')


def main() -> None:
    updater = Updater('YOUR_TOKEN_HERE')
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler('register', register))
    dispatcher.add_handler(CommandHandler('delete', delete))
    dispatcher.add_handler(CommandHandler('list', list_users))

    # Start the Bot
    updater.start_polling()  
    updater.idle()


if __name__ == '__main__':
    main()