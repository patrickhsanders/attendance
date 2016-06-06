from django.core.management.base import BaseCommand, CommandError
from attendance.models import Register, DailyStatistics
from people.models import Student
from django.utils import timezone
from datetime import datetime, timedelta

from ttt.settings import TIME_ZONE

class Command(BaseCommand):
    help = "Calculates the average arrival time of students."

    def add_arguments(self, parser):

        parser.add_argument('date',
                            nargs='?',
                            default=False,
                            type=str)


    def handle(self, *args, **options):

        if options['date'] != False:
            date = datetime.strptime(options['date'], "%Y%m%d").date()
        else:
            date = datetime.today()

        registers = Register.objects.filter(checkin__year=date.year, checkin__month=date.month, checkin__day=date.day)

        total_registers = len(registers)

        if total_registers == 0:
            self.stdout.write(self.style.ERROR("Statistics cannot be calculated."))
            return

        average_arrival_time = self.calculate_average_arrival_time(registers)
        self.stdout.write(self.style.SUCCESS("Average time: " + average_arrival_time.strftime("%H:%M")))

        registers_with_signout = [register for register in registers if register.forgot_to_checkout == False and register.checkout != None]
        total_registers_with_signout = len(registers_with_signout)

        average_spent_time = self.calculate_average_spent_time(registers_with_signout)
        self.stdout.write(self.style.SUCCESS("Average time: %.2f" % average_spent_time))

        total_students = Student.objects.filter(active=True).count()
        self.stdout.write(self.style.SUCCESS("Total students: " + str(total_students)))
        self.stdout.write(self.style.SUCCESS("Present students: " + str(total_registers)))

        percent_students_present = total_registers / total_students * 100
        self.stdout.write(self.style.SUCCESS("Percent present: %.0f%%" %percent_students_present))

        stats = DailyStatistics()
        stats.date = date
        stats.average_checkin = average_arrival_time
        stats.average_checkin_count = total_registers
        stats.average_hours_spent = average_spent_time
        stats.average_hours_spent_count = total_registers_with_signout
        stats.percent_students_present = percent_students_present
        stats.save()


    def calculate_average_arrival_time(self, registers):

        count_students_checked_in = 0
        total = 0

        for register in registers:
            count_students_checked_in += 1
            total += register.checkin.timestamp()

        if count_students_checked_in != 0:
            total = total / count_students_checked_in
            average_time = datetime.fromtimestamp(total)
            return average_time
        else:
            return False

    def calculate_average_spent_time(self, registers):

        count_students_checked_in = 0
        total = datetime.now() - datetime.now()

        for register in registers:
            count_students_checked_in += 1
            total += (register.checkout - register.checkin)

        if count_students_checked_in != 0:
            total_seconds = (total / count_students_checked_in).total_seconds()
            total_hours = total_seconds / 60 / 60
            return total_hours
        else:
            return False
