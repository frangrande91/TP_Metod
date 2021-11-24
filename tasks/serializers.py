from rest_framework import serializers
from tasks.models import Task, Board, Category

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'date', 'description'] # Campos que se serializan


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(many = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'tasks']  # Campos que se serializan


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many = True)
    class Meta:
        model = Board
        fields = ['id', 'name', 'categories']  # Campos que se serializan
