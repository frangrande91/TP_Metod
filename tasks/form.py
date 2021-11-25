from django import forms
from django.forms import ModelForm
from tasks.models import *




class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        boardid = kwargs.pop('boardid')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            queryset = Category.objects.filter(board_id=boardid),
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned': forms.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
