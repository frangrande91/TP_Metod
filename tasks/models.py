from enum import Enum

from django.db import models

# Create your models here.

"""
class Status(Enum):
    done = 'Done',
    inProgress = 'In progress',
    pending = 'Pending'
"""


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Board")

    def __str__(self):
        return self.name


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



