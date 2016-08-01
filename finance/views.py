from django.shortcuts import render
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from note.forms import NoteForm

from .forms import PaymentForm

from .models import StudentTuition

# Create your views here.


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