from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'date'] # Campos que se serializan