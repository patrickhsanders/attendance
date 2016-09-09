from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from people.models import Student
from .forms import RecruitForm, JobForm, CompanyForm, TaskForm, ResumeForm
from .models import Job, Recruit
# Create your views here.


class CreateEditRecruit(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"
    title = 'Edit Recruit Information'

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        recruit_form = RecruitForm(instance=student) if student.recruit is not None else RecruitForm()

        return render(request,
                      self.template_name,
                      {'form': recruit_form,
                       'title': self.title})

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
                {'form': recruit_form,
                 'title': self.title})


class CreateJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "create_job_form.html"
    title = 'Create Job'

    def get(self, request, recruit_id):
        job_form = JobForm()
        company_form = CompanyForm()

        return render(request,
                      self.template_name,
                      {'job_form': job_form,
                       'company_form': company_form,
                       'title': self.title})

    def post(self, request, recruit_id):
        job_form = JobForm(request.POST)
        company_form = CompanyForm(request.POST)

        if job_form.is_valid():
            job = job_form.save(commit=False)
            if job.company is None:
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
                           'company_form': company_form,
                           'title': self.title})


class EditJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "create_job_form.html"

    def get(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        job_form = JobForm(instance=job)
        company_form = CompanyForm()

        return render(request,
                      self.template_name,
                      {'job_form': job_form,
                       'company_form': company_form,
                       'job': job})

    def post(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        job_form = JobForm(request.POST, instance=job)
        company_form = CompanyForm(request.POST)

        if job_form.is_valid():
            job = job_form.save(commit=False)
            if job.company is None:
                if company_form.is_valid():
                    job.company = company_form.save()

            # TODO change this redirect
            job.save()
            return HttpResponseRedirect("/recruit/job")

        else:
            return render(request,
                      self.template_name,
                      {'job_form': job_form,
                       'company_form': company_form,
                       'job': job})


class CreateCompany(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"
    title = "Add Company"

    def get(self, request):
        company_form = CompanyForm()

        return render(request,
                      self.template_name,
                      {'company_form': company_form,
                       'title': self.title})

    def post(self, request):
        company_form = CompanyForm(request.POST)

        if company_form.is_valid():
            company_form.save()
            # TODO change this redirect
            return HttpResponseRedirect("/")
        else:
            return render(request,
                          self.template_name,
                          {'company_form': company_form,
                           'title': self.title})


class CreateResume(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"
    title = "Upload Resume"

    def get(self, request, recruit_id):
        recruit = get_object_or_404(Recruit, pk=recruit_id)
        self.title += " for " + recruit.student.first_name + " " + recruit.student.last_name
        form = ResumeForm()

        return render(request,
                      self.template_name,
                      {'form': form,
                       'title': self.title})

    def post(self, request, recruit_id):
        recruit = get_object_or_404(Recruit, pk=recruit_id)
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            recruit.resume.add(resume)
            return HttpResponseRedirect(recruit.student.get_absolute_url())

        return render(request,
                      self.template_name,
                      {'form': form,
                       'title': self.title})


class CreateTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_task'
    template_name = "recruit_generic_form.html"
    title = "Create Task"

    def get(self, request, recruit_id):
        form = TaskForm()

        return render(request,
                      self.template_name,
                      {'form': form,
                       'title': self.title})

    def post(self, request, recruit_id):
        pass


class JobsList(View):
    template_name = "job_list.html"

    def get(self, request):
        jobs = Job.objects.all()
        return render(request,
                      self.template_name,
                      {'jobs': jobs})


class DeleteJob(PermissionRequiredMixin, View):
    permission_required = 'recruit.delete_recruit'
    template_name = "delete_job.html"

    def get(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        return render(request,
                      self.template_name,
                      {'job': job})

    def post(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)
        job.delete()

        return HttpResponseRedirect("/recruit/job")