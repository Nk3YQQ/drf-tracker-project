from django.conf import settings
from telegram.ext import Updater, CommandHandler

from habit.services import start


def main():
    updater = Updater(settings.API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
