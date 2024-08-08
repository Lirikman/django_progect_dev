from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Problem, Article
from .permission import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import ArticleSerializer, ProblemSerializer


class ArticleApiView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsOwnerOrReadOnly]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAdminOrReadOnly]
        return [permission() for permission in permission_classes]


class ProblemApiView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (IsAdminUser,)
