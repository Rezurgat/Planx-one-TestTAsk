from django.db import models
from django.utils import timezone


class CurrentInfo(models.Model):
    activity_status = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True