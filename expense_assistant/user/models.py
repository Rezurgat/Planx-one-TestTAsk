from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_balance = models.DecimalField(default=0, max_digits=20, decimal_places=2)
