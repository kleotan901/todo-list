from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_created=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
        default=None,
        blank=True
    )

    def __str__(self):
        return self.content
