from django.urls import path
from django.views.generic import ListView

from tasks import views
# from tasks.views import CategoryList

urlpatterns = [
    path('list/', views.list_task, name="list"),
    path('update-task/<str:pk>/', views.TaskUpdate.as_view(), name="update_task"),
    path('delete-task/<str:pk>/', views.TaskDelete.as_view(), name="delete_task"),
    path('board-view/<str:pk>/', views.board_view, name="list-board-view"),
]
