from rest_framework import serializers
from tasks.models import Task, Board, Category

class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Board
        fields = ['id', 'name']  # Campos que se serializan


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    board = BoardSerializer()
    class Meta:
        model = Category
        fields = ['id', 'name', 'board']  # Campos que se serializan


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'date', 'description', 'status', 'assigned_id', 'category'] # Campos que se serializan


