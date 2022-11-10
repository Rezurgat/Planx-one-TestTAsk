from django.contrib import admin

from . import models


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ('amount', ' description', 'organization')