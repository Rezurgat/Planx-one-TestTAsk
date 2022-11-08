from django.db import models
from django.core.validators import MinValueValidator

from services.abstract_model import CurrentInfo
from user.models import User


class Category(CurrentInfo):
    title = models.CharField(default="", max_length=50)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} | {self.name}'