from django.core.management.base import BaseCommand, CommandError
from people.models import Student
from django.utils import timezone
from datetime import datetime
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError

from attendance.models import Register, ExcusedAbsence


class Command(BaseCommand):
    help = "Sends an email to Teddy with all students who are absent"

    def handle(self, *args, **options):
        active_students = Student.people.active().fulltime()
        today = datetime.today()

        known_absences = ExcusedAbsence.objects.filter(start_date__lte=today, end_date__gte=today)
        excused_absences = [absence.student for absence in known_absences]

        today_registers = Register.objects.filter(checkin__year=today.year, checkin__month=today.month, checkin__day=today.day)
        present_students = [register.student for register in today_registers]
        absent_students = [student for student in active_students if student not in present_students and student not in excused_absences]

        recipients = ["teddy@turntotech.io","ps@turntotech.io"]
        body_content = "Dear Teddy, the following students are absent today: \n\n"

        for student in absent_students:
            body_content += student.first_name + " " + student.last_name + "\n"

        try:
            send_mail("[TTT] Absent Students",body_content,"ps@turntotech.io",recipients)

        except BadHeaderError:
            self.add_error(None, ValidationError(
                'Could not send email, extra headers not allowed in email body.', code='badheader'
            ))
            return False
        # else:
        #     return True


