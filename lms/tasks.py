from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription


@shared_task
def send_course_update_mail(course):
    """Отправка писем об обновлении курса."""
    subscriptions = Subscription.objects.filter(course=course, is_subscribed=True)
    emails_list = []
    for subscription in subscriptions:
        emails_list.append(subscription.user.email)
    send_mail(
        subject="Обновление курса",
        message=f"Курс обновлён!",
        from_email=EMAIL_HOST_USER,
        recipient_list=emails_list,
        fail_silently=False,
    )
    print("Сообщения об обновлении курса отправлены!")
