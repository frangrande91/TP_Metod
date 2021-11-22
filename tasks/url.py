from django.urls import path
from django.views.generic import ListView

from tasks import views
# from tasks.views import CategoryList

urlpatterns = [
    # path('list/', views.list_task, name="list"),
    path('update-task/<str:pk>/', views.update_task, name="update_task"),
    path('delete-task/<str:pk>/', views.delete_task , name="delete_task"),
    path('category-add/<str:pk>/', views.CategoryCreate.as_view(), name="category-add"),
    path('board-view/<str:pk>/', views.board_view, name="board-view"),
    path('board-list/', views.BoardList.as_view(), name="board-list"),
    path('board-create/', views.BoardCreate.as_view(), name="board-create"),
    path('board-delete/<str:pk>/', views.BoardDelete.as_view(), name="board-delete"),
    path('board-update/<str:pk>/', views.BoardUpdate.as_view(), name="board-update"),

]
