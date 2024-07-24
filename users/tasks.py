import datetime

from celery import shared_task

import config.settings
from users.models import User


@shared_task
def check_users_activity():
    """Деактивирует пользователей, которые не заходили более 30 дней."""
    current_datetime = datetime.datetime.now(tz=config.settings.TIME_ZONE)
    deactivate_datetime = current_datetime - datetime.timedelta(days=30)
    users = User.objects.filter(last_login__lt=deactivate_datetime)
    for user in users:
        user.is_active = False
        user.save()
