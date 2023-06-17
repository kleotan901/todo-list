from django.urls import path, include

from task_list.views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
]

app_name = "task_list"
