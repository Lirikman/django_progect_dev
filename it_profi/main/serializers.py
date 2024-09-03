from datetime import datetime

from rest_framework import serializers
from .models import Article, Problem, Clients, Order


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = serializers.ImageField(default='main/info.jpg')

    class Meta:
        model = Article
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    problem = serializers.SlugRelatedField(queryset=Problem.active_objects.all(), slug_field='problem')

    class Meta:
        model = Order
        fields = ('id', 'client', 'phone', 'problem', 'is_active')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
