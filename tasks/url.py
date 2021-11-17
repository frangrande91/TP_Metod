from django.urls import path
from tasks import views

urlpatterns = [
    path('list/', views.index, name="list"),
    path('update-task/<str:pk>/', views.update_task, name="update_task"),
    path('delete-task/<str:pk>/', views.delete_task, name="delete_task")
]
