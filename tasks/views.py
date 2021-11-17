from django.shortcuts import render, redirect


from django.http import HttpResponse

from tasks.models import *
from .form import *
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView


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
    return render(request, 'tasks/list-task.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form': form}

    return render(request, 'tasks/update-task.html', context)

"""
def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    print(item)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete-task.html', context)"""

def get_current_path(request):
    return { 'current_path': request.get_full_path() }


class TaskDelete(DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/delete-task.html'
    success_url = '/tasks/board-view/'+"1"


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update-task.html'
    success_url = '/tasks/board-view/'+"1"


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





