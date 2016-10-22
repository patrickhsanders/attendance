from django.db import models
from django.utils import timezone
# Create your models here.


class NotificationPreferences(models.Model):

    disable_all_communication = models.BooleanField(default=False)
    receive_weekly_review = models.BooleanField(default=True)


class UnsubscribeToken(models.Model):

    student = models.ForeignKey('people.Student', null=True)
    token = models.CharField(max_length=31)


class NotificationLog(models.Model):

    recipient = models.ForeignKey('people.Student')
    sender = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=127, blank=True, null=True)
    content = models.TextField()
    fake = models.BooleanField(default=False)

    def __str__(self):
        output = "{} to {} {} from {} on {}".format(self.subject, self.recipient.first_name, self.recipient.last_name, self.sender, self.date)
        return output
