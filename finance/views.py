from calendar import month_name

from django.shortcuts import render
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from note.forms import NoteForm

from .forms import PaymentForm

from .models import StudentTuition, Payment
from django.utils import timezone
# Create your views here.


class PaymentsList(PermissionRequiredMixin, View):
    permission_required = 'finance.add_payment'
    template_name = "payment_list.html"

    def get(self, request):

        upcoming_payments = Payment.objects.filter(completed=False).order_by('date').prefetch_related('tuition')

        all_pending = Payment.objects.filter(completed=False)

        total_pending = 0.0
        for payment in all_pending:
            total_pending += payment.amount

        return render(request,
                      self.template_name,
                      {
                        'upcoming_payments': upcoming_payments,
                        'total_pending': total_pending
                      })


def get_month_from_offset(month, year, month_offset):
    if month_offset == 0:
        return (month, year)
    elif month_offset < 0:
        for x in range(month_offset, 0):
            if month != 1:
                month -= 1
            else:
                year -= 1
                month = 12
    elif month_offset > 0:
        for x in range(0, month_offset):
            if month != 12:
                month += 1
            else:
                year += 1
                month = 1

    return (month, year)


class MonthPaymentList(PermissionRequiredMixin, View):
    permission_required = 'finance.add_payment'
    template_name = "payment_list_portlet.html"

    def get(self, request):

        offset = self.request.GET.get('offset') if self.request.GET.get('offset') != None else 0

        now = timezone.now()
        month, year = get_month_from_offset(now.month, now.year, int(offset))

        payments_this_month = Payment.objects.filter(date__month=month, date__year=year).prefetch_related('tuition').order_by('date')

        total_payments = 0.0
        completed_payments = 0.0
        pending_payments = 0.0

        for payment in payments_this_month:
            total_payments += payment.amount
            if payment.completed is True:
                completed_payments += payment.amount
            else:
                pending_payments += payment.amount

        return render(request,
                      self.template_name,
                      {
                          'month': month_name[month],
                          'year': year,
                          'payments_this_month': payments_this_month,
                          'total_payments_this_month': total_payments,
                          'completed_payments_this_month': completed_payments,
                          'pending_payments_this_month': pending_payments,
                      })


class CreatePayment(PermissionRequiredMixin, View):
    permission_required = 'finance.add_payment'
    template_name = "payment.html"

    def get(self, request, tuition_id):

        payment_form = PaymentForm(prefix="PaymentForm")
        note_form = NoteForm(prefix="NoteForm")

        return render(request, self.template_name, {'payment_form':payment_form, 'note_form': note_form } )

    def post(self, request, tuition_id):

        tuition_object = get_object_or_404(StudentTuition, pk=tuition_id)

        payment_form = PaymentForm(request.POST, prefix="PaymentForm")
        note_form = NoteForm(request.POST, prefix="NoteForm")

        if payment_form.is_valid():
            payment = payment_form.save()
            tuition_object.payments.add(payment)
            tuition_object.save()

            if note_form.is_valid() and note_form.data['NoteForm-text']:
                note = note_form.save(commit=False)
                note.author = request.user
                note.save()
                tuition_object.notes.add(note)
                tuition_object.save()

            default_redirect = '/student/'
            redirect = request.GET.get('next') if request.GET.get('next') != None else default_redirect
            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'payment_form': payment_form, 'note_form': note_form})


class EditPayment(PermissionRequiredMixin, View):
    permission_required = 'finance.add_payment'
    template_name = "payment.html"

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, pk=payment_id)

        payment_form = PaymentForm(prefix="PaymentForm", instance=payment)
        note_form = NoteForm(prefix="NoteForm", instance=payment.notes)

        return render(request, self.template_name, {'payment_form': payment_form, 'note_form': note_form})

    def post(self, request, payment_id):
        payment = get_object_or_404(Payment, pk=payment_id)

        payment_form = PaymentForm(request.POST, prefix="PaymentForm", instance=payment)
        note_form = NoteForm(request.POST, prefix="NoteForm", instance=payment.notes)

        if payment_form.is_valid():
            payment = payment_form.save()

            if note_form.is_valid() and note_form.data['NoteForm-text']:
                note = note_form.save(commit=False)
                note.author = request.user
                note.save()

            default_redirect = '/finance/'
            redirect = request.GET.get('next') if request.GET.get('next') != None else default_redirect
            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'payment_form': payment_form, 'note_form': note_form})

