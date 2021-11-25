from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import csrf_token
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView

from user.forms import UserForm, LoginForm
from user.models import MyUser


def home(request):
    return redirect('board-list')


@csrf_exempt
def userLogin(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password) SOLO FUNCIONA CON SUPERUSER
        user = MyUser.objects.get(username=username)
        #if user is not None:
        if user.password == password:
            login(request, user)
            return redirect('board-list')

        else:
            messages.add_message(request, messages.INFO, 'Please log in.')
            return render(request, 'user/login.html')


"""#LOGIN CON FORMVIEW
class Login(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/home'"""


def userById(request, user_id):
    user = MyUser.objects.get(id=user_id)
    return render(request, 'user/profile.html', {'user': user})


class UserList(ListView):
    model = MyUser
    template_name = 'user/userList.html'
    queryset = User.objects.all()


class Register(CreateView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/register.html'
    success_url = '/user/userList'


def register(request):

    logout(request)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    context = {'form': form}

    return render(request, 'user/register.html', context)


class UserUpdate(UpdateView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/update.html'
    success_url = '/user/userList'


class UserDelete(DeleteView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/delete.html'
    success_url = '/user/userList'


class UserDetail(DetailView):
    model = MyUser
    template_name = 'user/friends.html'

