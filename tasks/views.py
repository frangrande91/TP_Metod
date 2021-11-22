from django.shortcuts import render, redirect
from .form import *
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

"""
def list_task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'tasks': tasks, 'form': form}
        return render(request, 'tasks/list-task.html', context)

    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list-task.html', context)"""


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/tasks/board-view/'+task.category.board.id.__str__())

    context = {'form': form}

    return render(request, 'tasks/update-task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/tasks/board-view/'+item.category.board.id.__str__())

    context = {'item': item}
    return render(request, 'tasks/delete-task.html', context)


class TaskDelete(DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/delete-task.html'
    success_url = '/tasks/board-view/'


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update-task.html'
    # success_url = '/tasks/board-view/'


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'tasks/register.html'
    success_url = '/user/userList'


def board_view(request, pk):
    board = Board.objects.get(id=pk)

    categories = board.categories.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'categories': categories, 'form': form}
        return render(request, 'tasks/board-view.html', context)

    form = TaskForm()
    context = {'categories': categories, 'form': form}
    return render(request, 'tasks/board-view.html', context)


class BoardList(ListView):
    model = Board
    template_name = 'tasks/board-list.html'
    queryset = Board.objects.all()


class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'tasks/board-create.html'
    success_url = '/tasks/board-list/'


class BoardDelete(DeleteView):
    model = Board
    form_class = BoardForm
    template_name = 'tasks/board-delete.html'
    success_url = '/tasks/board-list/'


class BoardUpdate(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'tasks/board-update.html'
    success_url = '/tasks/board-list/'

"""
class CategoryList(ListView):
    model = Category
    form_class = TaskForm
    template_name = 'tasks/board-view.html'
    queryset = Category.objects.all()


class TaskAdd(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/board-view.html'
    success_url = 'tasks/board-view.html'"""





