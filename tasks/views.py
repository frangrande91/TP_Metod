from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

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

########## CRUD TASK AND CATEGORY #########

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


"""class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'tasks/register.html'
<<<<<<< HEAD
    success_url = '/user/userList'"""

"""def categoryCreate(request, pk):
    if request.method == 'POST':
        formCategory = CategoryForm(request.POST)
        if formCategory.is_valid():
            formCategory.save()
            context = {'board_id': pk, 'form': formCategory}
            return render(request, 'tasks/board-view.html', context)
    formCategory = CategoryForm()
    context = {'board_id': pk, 'form': formCategory}
    return render(request, 'tasks/task-add.html', context)
"""

#INVESTIGAR CÓMO FILTRAR BOARDS Y CATEGORÍAS EN EL FORM
def board_view(request, pk):
    board = Board.objects.get(id=pk)
    categories = board.categories.all()


    if request.method == 'POST':
        form = TaskForm(request.POST)
        formCategory = CategoryForm(request.POST)

        #Add task
        if form.is_valid():
            form.save()
            context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board}
            return render(request, 'tasks/board-view.html', context)

        #Add category
        if formCategory.is_valid():
            formCategory.save()
            context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board}
            return render(request, 'tasks/board-view.html', context)



    form = TaskForm()
    formCategory = CategoryForm()
    context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board}
    return render(request, 'tasks/board-view.html', context)

def update_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/tasks/board-view/'+category.board.id.__str__())

    context = {'form': form}

    return render(request, 'tasks/update-category.html', context)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('/tasks/board-view/'+category.board.id.__str__())

    context = {'category': category}
    return render(request, 'tasks/delete-category.html', context)

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
    template_name = 'tasks/task-add.html'
    success_url = 'tasks/board-view.html'"""





