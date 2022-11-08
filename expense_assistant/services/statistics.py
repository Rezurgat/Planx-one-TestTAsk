from datetime import timedelta
from django.utils import timezone

from transactions.models import Transaction
from user.models import User


def latest_transactions(user):
    return len(
        Transaction.objects.filter(
            date__range=[timezone.now() - timedelta(days=1), timezone.now()],
            user__category=user,
        )
    )


def current_user_balance():
    return User.objects.first()