

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import path

from user.views import userById, UserUpdate, userLogin, register  # Login

from user.views import *


urlpatterns = [
    path('login/', userLogin, name='login'),
    #path('login/', Login.as_view()),
    path('logout', login_required(logout_then_login), name='logout'),
    path('<int:user_id>/', login_required(userById)),
    #path('userList/', UserList.as_view()),
    path('register/', register),
    #path('userList/', UserList.as_view()),
    path('register/', register, name='register'),
    path('update/<pk>', login_required(UserUpdate.as_view())),
    #path('delete/<pk>', login_required(UserDelete.as_view())),

    path('friends-list/<pk>', login_required(FriendList.as_view()), name='friends-list'),
    path('friends-add/', login_required(friends_add), name='friends-add'),
    path('friend-request-send/<str:pk>', login_required(friend_request_send), name='friend-request-send'),
    path('friend-request-confirm/<str:pk_friend>', login_required(friend_request_confirm), name='friend-request-confirm'),
    path('friend-request-reject/<str:pk_friend>', login_required(friend_request_reject), name='friend-request-reject'),

]

