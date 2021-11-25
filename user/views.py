from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import logout_then_login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import csrf_token
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView

from user.forms import UserForm, LoginForm
from user.models import MyUser, FriendRequest


def home(request):
    return redirect('board-list')


@csrf_exempt
def userLogin(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #user = authenticate(request, username=username, password=password) NO FUNCIONA
        user = User.objects.get(username=username)

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

"""
class UserList(ListView):
    model = MyUser
    template_name = 'user/userList.html'
    queryset = User.objects.all()"""

"""
class Register(CreateView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/register.html'
    success_url = '/tasks/board-list'"""


def register(request):
    logout(request)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail('Welcome '+request.POST['username']+' - TO DO LIST',
                      'Hi ' + request.POST['username']+'. Registered in TO DO LIST. Thanks for trusting us',
                      'operador.todolist@gmail.com', [request.POST['email']])

        return redirect('board-list')

    context = {'form': form}

    return render(request, 'user/register.html', context)


class UserUpdate(UpdateView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/update.html'
    success_url = '/tasks/board-list'

"""
class UserDelete(DeleteView):
    model = MyUser
    form_class = UserForm
    template_name = 'user/delete.html'
    success_url = '/user/login'"""


class FriendList(DetailView):
    model = MyUser
    template_name = 'user/friends-list.html'


def friends_add(request):
    item = None
    user_logged = MyUser.objects.get(pk=request.user.id)
    friends = user_logged.friends

    friend_requests_received = FriendRequest.objects.filter(receiver__id=user_logged.id)
    friend_requests_sent = FriendRequest.objects.filter(sender__id=user_logged.id)

    if request.method == 'POST':
        try:
            item = MyUser.objects.get(username=request.POST['username'])
            quantity_friends = friends.filter(username=item.username).count()
            quantity_requests_received = friend_requests_received.filter(sender__id=item.id).count()
            quantity_requests_sent = friend_requests_sent.filter(receiver__id=item.id).count()

            # Condiciones para que el usuario tenga posibilidad de mandar solicitud a otro usuario
            # No tiene que estar en su lista de amigos, y no tienen que tener solicitudes de amistad en comun pendientes
            if request.user.id != item.id and quantity_friends == 0 and quantity_requests_received == 0 and quantity_requests_sent == 0:
                context = {'item': item, 'friend_requests_received': friend_requests_received}
                return render(request, 'user/friends-add.html', context)
            else:
                item = None
        except MyUser.DoesNotExist:
            item = None

    context = {'item': item, 'friend_requests_received': friend_requests_received}
    return render(request, 'user/friends-add.html', context)


def friend_request_send(request, pk):
    sender = MyUser.objects.get(pk=request.user.id)
    friend_to_add = MyUser.objects.get(id=pk)
    context = {'friend_to_add': friend_to_add}

    if request.method == 'POST':
        friend_request = FriendRequest()
        friend_request.sender = sender
        friend_request.receiver = friend_to_add
        friend_request.save()

        send_mail('Friend request - TO DO LIST',
                  'User '+sender.username+'('+sender.email+') sent you a friend request on TO DO LIST. Login to your account to confirm',
                  'operador.todolist@gmail.com',
                  [friend_to_add.email])

        return redirect('/user/friends-add/')

    return render(request, 'user/friend-request-send.html', context)


def friend_request_confirm(request, pk_friend):
    try:
        receiver = MyUser.objects.get(pk=request.user.id)
        sender = MyUser.objects.get(pk=pk_friend)
        friend_request = FriendRequest.objects.get(receiver__id=receiver.id, sender__id=sender.id)

        if request.method == 'POST':
            receiver.friends.add(sender)
            sender.friends.add(receiver)
            receiver.save()
            sender.save()

            send_mail('Friend request accepted - TO DO LIST',
                      'User ' + receiver.username + '(' + receiver.email + ') accepted his friend request on TO DO LIST. Now you can share your projects',
                      'operador.todolist@gmail.com',
                      [sender.email])

            friend_request.delete()
            return redirect('/user/friends-add/')

        context = {'sender': sender}
        return render(request, 'user/friend-request-confirm.html', context)
    except MyUser.DoesNotExist:
        return redirect('/user/friends-add/')
    except FriendRequest.DoesNotExist:
        return redirect('/user/friends-add/')


def friend_request_reject(request, pk_friend):
    try:
        receiver = MyUser.objects.get(pk=request.user.id)
        sender = MyUser.objects.get(pk=pk_friend)
        friend_request = FriendRequest.objects.get(receiver__id=receiver.id, sender__id=sender.id)

        if request.method == 'POST':
            friend_request.delete()
            return redirect('/user/friends-add/')

        context = {'sender': sender}
        return render(request, 'user/friend-request-reject.html', context)
    except MyUser.DoesNotExist:
        return redirect('/user/friends-add/')
    except FriendRequest.DoesNotExist:
        return redirect('/user/friends-add/')
