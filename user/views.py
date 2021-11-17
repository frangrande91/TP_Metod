from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from user.forms import UserForm, LoginForm


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def userLogin(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')

        else:
            messages.add_message(request, messages.INFO, 'Please log in.')
            return render(request, 'user/login.html')

"""
#LOGIN CON FORMVIEW
class Login(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/home'
"""


def userById(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/profile.html', {'user' : user})


class UserList(ListView):
    model = User
    template_name = 'user/userList.html'
    queryset = User.objects.all()


class Register(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/register.html'
    success_url = '/user/userList'


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'
    success_url = '/user/userList'


class UserDelete(DeleteView):
    model = User
    form_class = UserForm
    template_name = 'user/delete.html'
    success_url = '/user/userList'