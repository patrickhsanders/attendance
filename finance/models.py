from django.db import models
from django.apps import apps
from note.models import Note


class Payment(models.Model):

    PAYMENT_TYPES = (('check', 'Check'),
                     ('cash', 'Cash'),
                     ('money order', 'Money Order'),
                     ('credit', 'Credit/Debit Card'),
                     ('deposit', 'EventBrite Deposit'),
                     ('wire', 'Wire transfer'),
                     ('discount', 'Discount'),
                     ('scholarship', 'Scholarship'))

    date = models.DateField()
    amount = models.FloatField()
    type = models.CharField(max_length=15, choices=PAYMENT_TYPES)
    reference = models.CharField(max_length=200,
                                 help_text="A reference number or other information pertanent to this transaction.",
                                 blank=True)
    notes = models.ForeignKey(Note, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):

        # StudentTuition = apps.get_model('finance', "StudentTuition")
        Student = apps.get_model('people', 'Student')

        try:
            student_tuition = StudentTuition.objects.get(payments=self)
            student = Student.objects.get(tuition=student_tuition)
            return "$" + str(self.amount) + " " + student.first_name + " " + student.last_name + " on " + str(self.date)
        except:
            pass

        return str(self.amount)


class StudentTuition(models.Model):
    tuition_total = models.FloatField()

    payments = models.ManyToManyField(Payment, blank=True)

    payed_in_full = models.BooleanField(default=False)
    notes = models.ManyToManyField(Note, blank=True)

    def __str__(self):

        Student = apps.get_model('people', 'Student')

        try:
            student = Student.objects.get(tuition=self)
            return str(self.tuition_total) + " " + student.first_name + " " + student.last_name
        except:
            pass

        return str(self.tuition_total)