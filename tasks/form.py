from django import forms
from django.forms import ModelForm
from tasks.models import *


class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        boardid = kwargs.pop('boardid')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            queryset = Category.objects.filter(board_id=boardid),
            widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['assigned'] = forms.ModelChoiceField(
            queryset = Board.objects.get(id=boardid).team.all() | MyUser.objects.filter(id=Board.objects.get(id=boardid).owner.id).all() #.add(Board.objects.get(id=boardid).owner),
            ,widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['assigned'].required = False


    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            #'assigned': forms.Select(attrs={'class': 'form-control', ''},)
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
