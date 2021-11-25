from django.contrib import admin

# Register your models here.
from user.models import MyUser, FriendRequest

admin.site.register(MyUser)
admin.site.register(FriendRequest)
