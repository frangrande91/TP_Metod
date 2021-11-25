

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import path
from user.views import userById, UserUpdate, userLogin, register, UserDetail  # Login

urlpatterns = [
    path('login/', userLogin, name='login'),
    #path('login/', Login.as_view()),
    path('logout', login_required(logout_then_login)),
    path('<int:user_id>/', login_required(userById)),
    #path('userList/', UserList.as_view()),
    path('register/', register),
    #path('userList/', UserList.as_view()),
    path('register/', register, name='register'),
    path('update/<pk>', login_required(UserUpdate.as_view())),
    #path('delete/<pk>', login_required(UserDelete.as_view())),
    path('detail/<pk>', login_required(UserDetail.as_view())),
]