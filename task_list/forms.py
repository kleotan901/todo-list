import datetime

from django import forms
from django.core.exceptions import ValidationError

from task_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    datetime = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "date"}),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["datetime"].initial = datetime.datetime.now()

    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline:
            if deadline.date() < datetime.date.today():
                raise ValidationError("Deadline can not be in the past")
        return deadline

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
