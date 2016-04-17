from django.core.management.base import BaseCommand, CommandError
from attendance.models import Register
from django.utils import timezone

class Command(BaseCommand):
    help = "Closes all open registers and flags them as having failed to checkout"

    def handle(self, *args, **options):
        open_registers = Register.objects.filter(checkout=None)

        for register in open_registers:
            register.forgot_to_checkout = True
            register.checkout = timezone.now()
            register.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed all open registers '))
