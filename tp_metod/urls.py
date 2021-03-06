"""tp_metod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from tasks.views import TaskViewSet
from rest_framework import routers
from tasks.models import Task

from user.views import home, userLogin#, Login

router = routers.DefaultRouter()
router.register(r'tasks_endpoint', TaskViewSet, basename=Task)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(home)),
    path('home/', login_required(home)),
    path('accounts/login/', userLogin),
    #path('accounts/login/', Login.as_view()),
    path('user/', include('user.urls')),
    path('tasks/', include('tasks.url')),
    path('', include(router.urls)), # URL endpoint http://localhost:8000/tasks
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # Auth para acceder al endpoint
]
