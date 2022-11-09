from django.core.mail import send_mail
from celery import shared_task

from user.models import User
from config.settings import EMAIL_HOST_USER
from services.statistics import latest_transactions, current_user_balance


@shared_task
def user_statistics():
    current_users = User.objects.filter(is_active=True, is_superuser=False)

    for user in current_users:
        latest_trans = latest_transactions(user)
        balance = current_user_balance(user)

        send_mail(
            "Your daily statistics from expense assistant!",
            f"Latest transactions {latest_trans}\n."
            f"Current balance - {balance}.",
            EMAIL_HOST_USER,
            [user.email],
        )