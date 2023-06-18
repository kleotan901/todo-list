from django.urls import path, include

from task_list.views import HomePage, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "task-list"
