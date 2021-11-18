from django import forms
from django.forms import ModelForm

from tasks.models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
