from django.urls import path, include

from task_list.views import HomePage, TaskCreateView, TaskUpdateView, TaskDeleteView, ChangeTaskStatus

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-status/", ChangeTaskStatus.as_view(), name="task-change-status"),
]

app_name = "task-list"
