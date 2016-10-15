from django.db import models
from django.utils import timezone

# from people.models import Student
# Create your models here.


class NotificationPreferences(models.Model):

    disable_all_communication = models.BooleanField(default=False)
    receive_weekly_review = models.BooleanField(default=True)


class UnsubscribeToken(models.Model):

    ninety_days_from_now = timezone.now() + timezone.timedelta(days=90)

    token = models.CharField(max_length=31)
    expiration_date = models.DateField()


class NotificationLog(models.Model):

    recipient = models.ForeignKey('people.Student')
    sender = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=127, blank=True, null=True)
    content = models.TextField()
    fake = models.BooleanField(default=False)

    def __str__(self):
        recipients = ', '.join(self.recipient)
        output = "{} to {} from {} on {}".format(self.subject, recipients, self.sender, self.date)
