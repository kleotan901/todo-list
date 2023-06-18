from django import forms

from task_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    datetime = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    deadline = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
