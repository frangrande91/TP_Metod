from django.contrib import admin

# Register your models here.
from tasks.models import *

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Board)

