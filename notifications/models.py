from django.db import models
from django.utils import timezone
# Create your models here.


class NotificationPreferences(models.Model):

    disable_all_communication = models.BooleanField(default=False)
    receive_weekly_review = models.BooleanField(default=True)


class UnsubscribeToken(models.Model):

    ninety_days_from_now = timezone.now() + timezone.timedelta(days=90)

    token = models.CharField(max_length=31)
    expiration_date = models.DateField()