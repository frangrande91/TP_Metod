

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import path
from user.views import userById, UserList, Register, UserUpdate, UserDelete, userLogin #Login

urlpatterns = [
    path('login/', userLogin),
    #path('login/', Login.as_view()),
    path('logout', logout_then_login),
    path('<int:user_id>/', userById),
    path('userList/', UserList.as_view()),
    path('register/', Register.as_view()),
    path('update/<pk>', UserUpdate.as_view()),
    path('delete/<pk>', UserDelete.as_view()),
]