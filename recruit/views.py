from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect

from people.models import Student
from .forms import RecruitForm
# Create your views here.


class CreateEditRecruit(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        recruit_form = RecruitForm(instance=student) if student.recruit is not None else RecruitForm()

        return render(request,
                      self.template_name,
                      {'recruit_form': recruit_form})

    def put(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        recruit_form = RecruitForm(request.POST, instance=student) \
                        if student.recruit is not None \
                        else RecruitForm(request.POST)

        if recruit_form.is_valid():
            recruit_form.save()
            return HttpResponseRedirect(student.get_absolute_url())


        return render(request,
                      self.template_name,
                      {'recruit_form': recruit_form})


class CreateJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def put(self, request):
        pass


class EditJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def put(self, request):
        pass


class CreateCompany(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def put(self, request):
        pass


class CreateResume(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def put(self, request):
        pass


class CreateTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def put(self, request):
        pass