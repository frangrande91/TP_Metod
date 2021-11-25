from django import forms
from django.forms import ModelForm

from tasks.models import *




class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned': forms.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'board': forms.Select(attrs={'class': 'form-control'})
        }


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
