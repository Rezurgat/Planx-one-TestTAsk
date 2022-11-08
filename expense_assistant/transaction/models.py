from django.core.validators import MinValueValidator
from django.db import models

from category.models import Category
from services.abstract_model import CurrentInfo


class Transaction(CurrentInfo):
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    description = models.TextField(blank=True)
    organization = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} | {self.amount}'