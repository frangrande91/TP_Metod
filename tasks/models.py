from enum import Enum

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import TextChoices

from user.models import MyUser


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Board")
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='boards')

    def __str__(self):
        return self.name

    @staticmethod
    def is_owner(self, user):
        is_owner = False

        if user.id == self.owner.id:
            is_owner = True

        return is_owner

        # A partir del id de un board retorna una lista con el owner y los colaboradores del tablero

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

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Category")
    board = models.ForeignKey(Board,  on_delete=models.CASCADE, null=True, related_name='categories')

    def __str__(self):
        return self.name



class Task(models.Model):

    class Status(TextChoices):
        toDo = 'To do'
        inProgress = 'In progress'
        done = 'Done'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.toDo)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='tasks')
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, default='')
    assigned = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title





