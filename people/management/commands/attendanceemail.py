import random
import pytz

from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives, send_mass_mail, get_connection
from django.template.loader import get_template
from django.template import Context

from people.models import Student
from attendance.models import DailyAttendance, Register

from people.views import get_completion_calendar
from notifications.utils import get_or_create_notification_preferences_for_student
from notifications.models import NotificationLog

from ...constants import WEEKLY_ATTENDANCE_SUBJECT


class Command(BaseCommand):

    HELLO_OPTIONS = ['Hey',
                     'Hello',
                     'Hi',
                     'Howdy',
                     'Bonjour',
                     'Greetings']

    POSITIVE_MESSAGE = ['good going!',
                        'excellent!',
                        'keep up the good work!']

    NEGATIVE_MESSAGE = ['hopefully we\'ll see you more next week.',]

    SIGNOFFS = ['Stay classy',
                '01100010 01111001 01100101',
                'adbb',
                '😄',
                'Hope to see you soon']

    REACH_OUT = ['']


    help = "Send attendance email on Fridays"

    def add_arguments(self, parser):

        parser.add_argument(
            '-d', '--debug',
            action='store_true',
            dest='debug',
            default=False,
            help='Add migrations to run',
        )

    def get_monday(self):
        date = timezone.now() - timedelta(days=2) - timedelta(days=5)
        return date

    def handle(self, *args, **options):

        date = timezone.now()
        tz = pytz.timezone("US/Eastern")
        day_of_week = tz.normalize(date).weekday()

        if day_of_week == 5 or options['debug']:

            self.stdout.write(self.style.SUCCESS("We can run this now"))
            plaintext_email = get_template('email/attendance_plain_email.txt')
            html_email = get_template('email/attendance_html_email.html')

            students = Student.people.active().fulltime()[:1]

            emails = []

            self.get_monday()

            attendances_last_five_days = DailyAttendance.objects.filter(date__gte=self.get_monday()).order_by('date')

            for student in students:

                student_email_preferences = get_or_create_notification_preferences_for_student(student)
                if student_email_preferences.disable_all_communication or not student_email_preferences.receive_weekly_review:
                    self.stdout.write(self.style.ERROR("Skipping " +
                                                       student.first_name +
                                                       " " +
                                                       student.last_name +
                                                       " because they have opted out of receiving this email."))
                    continue

                days_present = 0
                days_absent = 0

                for attenance in attendances_last_five_days:
                    if attenance.present.filter(pk=student.pk).exists():
                        days_present += 1
                    else:
                        days_absent += 1

                print(student.first_name + " " + str(days_present) + " | " + str(days_absent))

                projects, day = get_completion_calendar(student)

                remaining_projects_count = len(projects)

                days_message = random.choice(self.POSITIVE_MESSAGE) if days_present >= 3 else random.choice(self.NEGATIVE_MESSAGE)

                recipient = student.email if not options['debug'] else 'patrickhsanders@gmail.com'

                context = {'student': student,
                           'first_name': student.first_name,
                           'greeting': random.choice(self.HELLO_OPTIONS),
                           'signoff': random.choice(self.SIGNOFFS),
                           'current_project': student.current_project,
                           'remaining_projects': projects,
                           'remaining_projects_count': remaining_projects_count,
                           'days_message': days_message,
                           'days_present': days_present,
                           'days_absent': days_absent,
                           'recipient': recipient}

                text_content = plaintext_email.render(context)
                html_content = html_email.render(context)

                email = EmailMultiAlternatives(
                    WEEKLY_ATTENDANCE_SUBJECT,
                    text_content,
                    'TurnToTech <nyc@turntotech.io>',
                    [recipient],
                )
                email.attach_alternative(html_content, "text/html")
                emails.append(email)

                # Create log of email notification
                NotificationLog.objects.create(recipient=recipient,
                                               sender='weekly_attendance_saturday',
                                               subject=WEEKLY_ATTENDANCE_SUBJECT,
                                               content=text_content + "\n\n\n" + html_content)

            connection = get_connection()
            connection.send_messages(emails)
            connection.close()

        else:
            self.stdout.write(self.style.ERROR("This script can only run on Saturday."))

