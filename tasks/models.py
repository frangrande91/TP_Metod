from enum import Enum

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from user.models import MyUser

"""
class Status(Enum):
    done = 'Done',
    inProgress = 'In progress',
    pending = 'Pending'
"""


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


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Category")
    board = models.ForeignKey(Board,  on_delete=models.CASCADE, null=True, related_name='categories')

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # status = models.ForeignKey(Status, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='tasks')
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title





