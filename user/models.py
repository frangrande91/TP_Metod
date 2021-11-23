from django.contrib.auth.models import User
from django.db import models

import tasks
# from tasks.models import Board


class MyUser(User):
    boardsToCollaborate = models.ManyToManyField('tasks.Board', blank=True, related_name='team')


    def is_collaborate(self, user):

        for userToCheck in self.boardsToCollaborate.get(all()):

             is_owner = False

        if user.id == self.owner.id:
            is_owner = True

        return is_owner

