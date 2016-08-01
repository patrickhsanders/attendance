from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .forms import NoteForm
from .models import Note

from .forms import NoteForm

# detached notes don't make sense
#
# class CreateNote(PermissionRequiredMixin, View):
#     permission_required = 'note.add_note'
#     template_name = "create_update_note.html"
#     default_redirect = '/student/list/job-status/'
#
#     def get(self, request):
#         form = NoteForm()
#         return render(request, self.template_name, {'form': form })
#
#     def post(self, request):
#         bound_form = NoteForm(request.POST)
#
#         if bound_form.is_valid():
#             obj = bound_form.save(commit=False)
#             obj.author = request.user
#             obj.save()
#
#         redirect = request.GET.get('next') if request.GET.get('next') != None else self.default_redirect
#         return HttpResponseRedirect(redirect)


class UpdateNote(PermissionRequiredMixin, View):
    permission_required = 'note.add_note'
    template_name = "create_update_note.html"
    default_redirect = '/student/list/job-status/'

    def get(self, request, note_id):
        note = get_object_or_404(Note, pk=note_id)
        form = NoteForm(instance=note)
        return render(request, self.template_name, {'form': form})

    def post(self, request, note_id):
        note = get_object_or_404(Note, pk=note_id)
        bound_form = NoteForm(request.POST, instance=note)

        if bound_form.is_valid():
            bound_form.save()

        redirect = request.GET.get('next') if request.GET.get('next') != None else self.default_redirect
        return HttpResponseRedirect(redirect)


class DeleteNote(PermissionRequiredMixin, View):
    permission_required = 'note.add_note'
    template_name = "delete_note_confirmation.html"
    default_redirect = '/student/list/job-status/'

    def get(self, request, note_id):
        return render(request, self.template_name)

    def post(self, request, note_id):
        note = get_object_or_404(Note, pk=note_id)
        note.delete()
        # note.soft_delete = True
        # note.save()

        redirect = request.GET.get('next') if request.GET.get('next') != None else self.default_redirect
        return HttpResponseRedirect(redirect)

