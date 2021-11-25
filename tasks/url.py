from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import ListView

from tasks import views
# from tasks.views import CategoryList
from user.views import home

urlpatterns = [
    # path('list/', views.list_task, name="list"),
    path('home/', login_required(home)),
    path('update-task/<str:pk>/', login_required(views.update_task), name="update_task"),
    path('delete-task/<str:pk>/', login_required(views.delete_task), name="delete_task"),
    #path('add-task/<str:pk>', views.TaskAdd, name="task-add")
    #path('category-add/<str:pk>/', views.CategoryCreate.as_view(), name="category-add"),
    path('board-view/<str:pk>/', login_required(views.board_view), name="board-view"),
    path('update-category/<str:pk>/', login_required(views.update_category), name="update_category", ),
    path('delete-category/<str:pk>/', login_required(views.delete_category), name="delete_category"),
    path('board-list/', login_required(views.board_list), name="board-list"),
    path('board-create/', login_required(views.BoardCreate.as_view()), name="board-create"),
    path('board-delete/<str:pk>/', login_required(views.BoardDelete.as_view()), name="board-delete"),
    path('board-update/<str:pk>/', login_required(views.board_update), name="board-update"),
    path('board-collaboration-exit/<str:pk_board>/', login_required(views.board_collaborate_exit), name="board-collaboration-exit"),
]
