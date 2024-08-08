from datetime import datetime

from rest_framework import serializers
from .models import Article, Problem


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_active = serializers.HiddenField(default=False)
    date = serializers.HiddenField(default=datetime.now)

    class Meta:
        model = Article
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
