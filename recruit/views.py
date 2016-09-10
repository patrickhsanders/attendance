from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.utils import timezone

from people.models import Student
from .forms import RecruitForm, JobForm, CompanyForm, TaskForm, ResumeForm
from .models import Job, Recruit, Task
# Create your views here.


class CreateEditRecruit(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_recruit'
    template_name = "recruit_generic_form.html"
    title = 'Edit Recruit Information'

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        recruit_form = RecruitForm(instance=student.recruit) if student.recruit != None else RecruitForm()

        return render(request,
                      self.template_name,
                      {'form': recruit_form,
                       'title': self.title})

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        if student.recruit != None:
            recruit_form = RecruitForm(request.POST, instance=student.recruit)
        else:
            recruit_form = RecruitForm(request.POST)

        if recruit_form.is_valid():
            recruit = recruit_form.save()
            student.recruit = recruit
            student.save()
            return HttpResponseRedirect(student.get_recruit_url())

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


class TaskList(View):
    template_name = "task_list.html"

    def get(self, request):
        tasks = Task.objects.all().order_by('date_to_finish_by')
        return render(request,
                      self.template_name,
                      {'tasks': tasks})


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
        recruit = get_object_or_404(Recruit, pk=recruit_id)
        print(recruit.student)
        print("HELLO")

        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            recruit.tasks.add(task)
            recruit.save()
            return HttpResponseRedirect(recruit.student.get_recruit_url())

        else:
            return render(request,
                      self.template_name,
                      {'form': form,
                       'title': self.title})


class EditTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_task'
    template_name = "edit_task.html"
    title = "Edit Task"

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)

        return render(request,
                      self.template_name,
                      {'form': form,
                       'title': self.title,
                       'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect(task.recruit_set.first().student.get_recruit_url())

        else:
            return render(request,
                          self.template_name,
                          {'form': form,
                           'title': self.title,
                           'task': task})

class CompleteTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.add_task'

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.completed = True
        task.completed_date = timezone.now()
        task.save()
        return HttpResponseRedirect(task.recruit_set.first().student.get_recruit_url())


class DeleteTask(PermissionRequiredMixin, View):
    permission_required = 'recruit.delete_recruit'
    template_name = "delete_task.html"

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request,
                      self.template_name,
                      {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        student = task.recruit_set.all().first().student
        task.delete()

        return HttpResponseRedirect(student.get_absolute_url())



