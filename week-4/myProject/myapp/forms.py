from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title']  # use only title if you want to add tasks

class TodoSearchForm(forms.Form):
    query = forms.CharField(label='Search for a task', max_length=200, required=False)
