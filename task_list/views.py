from django.urls import reverse_lazy
from django.views import generic

from task_list.forms import TaskForm
from task_list.models import Task, Tag


class HomePage(generic.ListView):
    template_name = "task_list/index.html"
    queryset = Task.objects.all()
    context_object_name = "task_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
