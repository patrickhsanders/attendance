from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from django.conf import settings

from notifications.models import NotificationLog

class Command(BaseCommand):
    help = "Remove all notification logs before a specific date."

    def handle(self, *args, **options):

        today = timezone.now()
        if settings.DAYS_OF_LOGS_TO_KEEP:
            self.stdout.write(self.style.SUCCESS("Deleting notification records older than " + str(settings.DAYS_OF_LOGS_TO_KEEP) + " days"))
            delete_before_day = timezone.now() - timezone.timedelta(days=settings.DAYS_OF_LOGS_TO_KEEP)
            notifications_to_delete = NotificationLog.objects.filter(date__lt=delete_before_day)

            self.stdout.write(self.style.SUCCESS("Deleting " + str(notifications_to_delete.count())))
            for notification in notifications_to_delete:
                self.stdout.write(self.style.SUCCESS(" - Deleting " + notification))
                notification.delete()

        self.stdout.write(self.style.SUCCESS("Task Finished"))