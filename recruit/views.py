from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from people.models import Student
from .forms import RecruitForm, JobForm, CompanyForm
from .models import Job, Recruit
# Create your views here.


class CreateEditRecruit(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        recruit_form = RecruitForm(instance=student) if student.recruit is not None else RecruitForm()

        return render(request,
                      self.template_name,
                      {'form': recruit_form})

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        recruit_form = RecruitForm(request.POST, instance=student) \
                        if student.recruit is not None \
                        else RecruitForm(request.POST)

        if recruit_form.is_valid():
            recruit = recruit_form.save()
            student.recruit = recruit
            student.save()
            return HttpResponseRedirect(student.get_absolute_url())

        else:
            return render(request,
                self.template_name,
                {'form': recruit_form})


class CreateJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "create_job_form.html"

    def get(self, request, recruit_id):
        job_form = JobForm()
        company_form = CompanyForm()

        return render(request,
                      self.template_name,
                      {'job_form': job_form,
                       'company_form': company_form})

    def post(self, request, recruit_id):
        job_form = JobForm(request.POST)
        company_form = CompanyForm(request.POST)

        if job_form.is_valid():
            job = job_form.save(commit=False)

            try:
                (job.company is not None)
            except:
                if company_form.is_valid():
                    job.company = company_form.save()

            job.save()
            recruit = get_object_or_404(Recruit, pk=recruit_id)
            recruit.jobs.add(job)
            recruit.save()

            return HttpResponseRedirect(recruit.student.get_absolute_url())

        else:
            return render(request,
                          self.template_name,
                          {'job_form': job_form,
                           'company_form': company_form})


class EditJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def post(self, request):
        pass


class CreateCompany(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def post(self, request):
        pass


class CreateResume(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def post(self, request):
        pass


class CreateTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'

    def get(self, request):
        pass

    def post(self, request):
        pass