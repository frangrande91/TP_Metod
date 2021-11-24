

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import path
from user.views import userById, UserList, Register, UserUpdate, UserDelete, userLogin, register  # Login

urlpatterns = [
    path('login/', userLogin),
    #path('login/', Login.as_view()),
    path('logout', login_required(logout_then_login)),
    path('<int:user_id>/', login_required(userById)),
    #path('userList/', UserList.as_view()),
    path('register/', register),
    path('update/<pk>', login_required(UserUpdate.as_view())),
    path('delete/<pk>', login_required(UserDelete.as_view())),
]