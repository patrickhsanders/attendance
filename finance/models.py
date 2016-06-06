from django.db import models
from people.models import Student
# Create your models here.


class Payment(models.Model):

    PAYMENT_TYPES = (('check', 'Check'),
                     ('credit', 'Credit card'),
                     ('wire', 'Wire transfer'),
                     ('discount', 'Discount'),
                     ('scholarship', 'Scholarship'))

    date = models.DateField()
    amount = models.FloatField()
    type = models.CharField(max_length=15, choices=PAYMENT_TYPES)
    reference = models.CharField(max_length=200, help_text="A reference number or other information pertanent to this transaction.")

    #note of new type

class StudentTuition(models.model):

    student = models.ForeignKey(Student)
    tuition_total = models.FloatField()
    payments = models.ManyToManyField(Payment, blank=True)

    #note of new type
    #reminder of new type