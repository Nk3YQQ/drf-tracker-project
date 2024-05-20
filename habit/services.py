from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from telegram import Update, Bot
from telegram.ext import CallbackContext

from users.models import User


def start(update: Update, context: CallbackContext) -> None:
    """Функция запускает общение пользователя с ботом"""

    args = context.args

    if args:
        tg_token = args[0]

        try:

            user = User.objects.get(tg_token=tg_token)
            user.chat_id = update.message.chat_id
            user.save()

            context.bot.send_message(chat_id=update.message.chat_id, text="Регистрация подтверждена!")

        except ObjectDoesNotExist:
            context.bot.send_message(chat_id=update.message.chat_id, text="Неверный токен!")

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Токен не предоставлен!")


def make_a_notify(mode=None):
    """Функция для рассылки уведомлений о привычках"""

    periodicity = "ежедневных" if mode == "daily" else "еженедельных"

    users = User.objects.filter(is_superuser=False)

    bot = Bot(token=settings.API_TOKEN)

    for user in users:
        chat_id = user.chat_id

        habits = (
            user.habits.filter(periodicity="daily") if mode == "daily" else user.habits.filter(periodicity="weekly")
        )

        message = f"Напоминание о {periodicity} привычках, которые Вам необходимо сделать:\n\n"

        for habit in habits:
            message += f"- {habit}\n"

        bot.send_message(chat_id=chat_id, text=message)

        send_mail(
            subject="Напоминание о привычки!",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
