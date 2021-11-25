from django.contrib import messages
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

    task = Task.objects.get(id=pk)  # obtengo la tarea a editar
    board = task.category.board  # obtengo el tablero al que pertenece la tarea
    myUser = MyUser.objects.get(id=request.user.id)  # MyUser logueado
    boards = myUser.boardsToCollaborate.all()  # obtengo todos los tableros en los que el usuario es colaborador

    if board.owner == myUser or board in boards:  # Valido que el usuario sea el dueño o un coladorador del tablero a la que pertenece la categoría a editar

        form = TaskForm(instance=task, boardid=task.category.board.id)

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task, boardid=task.category.board.id)
            if form.is_valid():
                form.save()
            return redirect('/tasks/board-view/' + task.category.board.id.__str__())

        context = {'form': form}

        return render(request, 'tasks/update-task.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Access denied')
        return redirect('/tasks/board-list/')


def delete_task(request, pk):
    item = Task.objects.get(id=pk)  # obtengo la tarea a eliminar
    board = item.category.board  # obtengo el tablero al que pertenece la tarea
    myUser = MyUser.objects.get(id=request.user.id)  # MyUser logueado
    boards = myUser.boardsToCollaborate.all()  # obtengo todos los tableros en los que el usuario es colaborador

    if board.owner == myUser or board in boards:  # Valido que el usuario sea el dueño o un coladorador del tablero a la que pertenece la categoría a eliminar

        if request.method == 'POST':
            item.delete()
            return redirect('/tasks/board-view/' + item.category.board.id.__str__())

        context = {'item': item}
        return render(request, 'tasks/delete-task.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Access denied')
        return redirect('/tasks/board-list/')


"""
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

def categoryCreate(request, pk):
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
    board = Board.objects.get(id=pk)    #obtengo el tablero pedido
    myUser = MyUser.objects.get(id=request.user.id)    #MyUser logueado
    boards = myUser.boardsToCollaborate.all()    #obtengo todos los tableros en los que el usuario es colaborador
    collaborators = getTeamBoard(pk)

    if board.owner == myUser or board in boards:  # Valido que el usuario que está viendo el tablero sea el dueño o un coladorador

        categories = board.categories.all()

        if request.method == 'POST':
            form = TaskForm(request.POST, boardid=pk)
            formCategory = CategoryForm(request.POST)

            # Add task
            if form.is_valid():
                form.save()
                context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board, 'collaborators': collaborators}
                return render(request, 'tasks/board-view.html', context)

            # Add category
            if formCategory.is_valid():

                category = formCategory.save()
                category.board = board
                category.save()
                context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board}
                return render(request, 'tasks/board-view.html', context)

        form = TaskForm(request.POST, boardid=pk)
        formCategory = CategoryForm(request.POST)
        context = {'categories': categories, 'form': form, 'formCategory': formCategory, 'board': board}
        return render(request, 'tasks/board-view.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Access denied')
        return redirect('/tasks/board-list/')


#A partir del id de un board retorna una lista con el owner y los colaboradores del tablero
def getTeamBoard(pk_board):
    board = Board.objects.get(pk=pk_board)
    owner = board.owner
    teamList = [owner]
    users = MyUser.objects.all()

    for user in users:
        boards = user.boardsToCollaborate.all()
        for b in boards:
            if b == board:
                teamList.append(user)

    return teamList



def update_category(request, pk):
    category = Category.objects.get(id=pk)  # obtengo la categoria a editar
    board = category.board  # obtengo el tablero al que pertenece la categoria
    myUser = MyUser.objects.get(id=request.user.id)  # MyUser logueado
    boards = myUser.boardsToCollaborate.all()  # obtengo todos los tableros en los que el usuario es colaborador

    if board.owner == myUser or board in boards:  # Valido que el usuario sea el dueño o un coladorador del tablero a la que pertenece la categoría a editar

        form = CategoryForm(instance=category)

        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
            return redirect('/tasks/board-view/' + category.board.id.__str__())
        context = {'form': form}
        return render(request, 'tasks/update-category.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Access denied')
        return redirect('/tasks/board-list/')


def delete_category(request, pk):
    category = Category.objects.get(id=pk)  # obtengo la categoria a eliminar
    board = category.board  # obtengo el tablero al que pertenece la categoria
    myUser = MyUser.objects.get(id=request.user.id)  # MyUser logueado
    boards = myUser.boardsToCollaborate.all()  # obtengo todos los tableros en los que el usuario es colaborador

    if board.owner == myUser or board in boards:  # Valido que el usuario sea el dueño o un coladorador del tablero a la que pertenece la categoría a eliminar

        if request.method == 'POST':
            category.delete()
            return redirect('/tasks/board-view/' + category.board.id.__str__())

        context = {'category': category}
        return render(request, 'tasks/delete-category.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Access denied')
        return redirect('/tasks/board-list/')


def board_list(request):
    user = MyUser.objects.get(id=request.user.id)
    own = Board.objects.filter(owner__id=user.id)
    collaborations = user.boardsToCollaborate.all()

    context = {'own': own, 'collaborations': collaborations}

    return render(request, 'tasks/board-list.html', context)


def board_update(request, pk):
    board = Board.objects.get(id=pk)
    user = MyUser.objects.get(pk=request.user.id)

    if board.owner.id == user.id:

        if request.method == 'POST':
            board.name = request.POST['name']
            board.save()


        friends = user.friends.all()
        context = {'board': board, 'friends': friends}
        return render(request, 'tasks/board-update.html', context)

    return render(request, 'tasks/board-list.html')



"""
class BoardList(ListView):
    model = Board
    template_name = 'tasks/board-list.html'
    # queryset = Board.objects.all()

    def get_queryset(self):
        own = Board.objects.filter(owner= self.request.user.id)
        myuser = MyUser.objects.get(user_ptr_id = self.request.user.id)
        collab = myuser.boardsToCollaborate.all()
        return own | collab
"""


class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'tasks/board-create.html'
    success_url = '/tasks/board-list/'

    def form_valid(self, form):
        board = form.save(commit=False)
        board.owner_id = self.request.user.id
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model
        board.save()
        return super().form_valid(form)


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
