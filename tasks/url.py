from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import ListView

from tasks import views
# from tasks.views import CategoryList

urlpatterns = [
    # path('list/', views.list_task, name="list"),
    path('update-task/<str:pk>/', login_required(views.update_task), name="update_task"),
    path('delete-task/<str:pk>/', login_required(views.delete_task), name="delete_task"),
    #path('add-task/<str:pk>', views.TaskAdd, name="task-add")
    #path('category-add/<str:pk>/', views.CategoryCreate.as_view(), name="category-add"),
    path('board-view/<str:pk>/', login_required(views.board_view), name="board-view"),
    path('update-category/<str:pk>/', login_required(views.update_category), name="update_category", ),
    path('delete-category/<str:pk>/', login_required(views.delete_category), name="delete_category"),
    path('board-list/', login_required(views.BoardList.as_view()), name="board-list"),
    path('board-create/', login_required(views.BoardCreate.as_view()), name="board-create"),
    path('board-delete/<str:pk>/', login_required(views.BoardDelete.as_view()), name="board-delete"),
    path('board-update/<str:pk>/', login_required(views.BoardUpdate.as_view()), name="board-update"),
    path('board-update/<str:pk>/', login_required(views.BoardUpdate.as_view()), name="board-update"),
]
