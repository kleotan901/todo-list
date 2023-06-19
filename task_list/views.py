import datetime

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views import generic

from task_list.forms import TaskForm, TagForm
from task_list.models import Task, Tag


class HomePage(generic.ListView):
    template_name = "task_list/index.html"
    queryset = Task.objects.all()
    context_object_name = "task_list"
    ordering = ["is_completed", "-datetime"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        for task in context["task_list"]:
            task.datetime = task.datetime.strftime("%B %d, %Y, %I:%M %p")
            if task.deadline:
                task.deadline = task.deadline.strftime("%B %d, %Y, %I:%M %p")
        return context


class ChangeTaskStatus(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return HttpResponseRedirect(reverse_lazy("task_list:index"))

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Invalid request method.")

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_list:index")


class TagListView(generic.ListView):
    model = Tag

class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_list:tag-list")
