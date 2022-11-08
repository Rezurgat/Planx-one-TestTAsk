from django.core.mail import send_mail
from celery import shared_task

from user.models import User
from config.settings import EMAIL_HOST_USER
from services.statistics import latest_transactions, current_user_balance


@shared_task
def user_statistics():
    current_users = User.objects.filter(is_active=True, is_superuser=False)

    for user in active_users:
        amount_trans = count_transactions(user)
        most_popular_category = find_the_most_popular_category(user)

        send_mail(
            "Your daily statistics from expense assistant!",
            f"Total transactions {amount_trans}\n."
            f"Most popular category - {most_popular_category[0]} with amount {most_popular_category[1]}.",
            EMAIL_HOST_USER,
            [user.email],
        )