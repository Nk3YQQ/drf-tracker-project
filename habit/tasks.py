from celery import shared_task

from habit.services import make_a_notify


@shared_task
def notify_users_with_oneday_habit():
    """ Задача уведомляет пользователей, у которых
    привычку необходимо выполнять раз в день """

    make_a_notify(mode='daily')


@shared_task
def notify_users_with_weekly_habit():
    """ Задача уведомляет пользователей, у которых
    привычку необходимо выполнять раз в неделю """

    make_a_notify(mode='weekly')
