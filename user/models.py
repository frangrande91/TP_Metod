from django.contrib.auth.models import User
from django.db import models

import tasks


# from tasks.models import Board


class MyUser(User):
    boardsToCollaborate = models.ManyToManyField('tasks.Board', blank=True, related_name='team')
    friends = models.ManyToManyField('user.MyUser', blank=True)


class FriendRequest(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='requestsSent')
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='requestsReceived')

    """def is_collaborate(self, user):
        is_collaborate = False

        for userToCheck in self.boardsToCollaborate.get(all()):
            is_collaborate = False

        return is_collaborate"""
