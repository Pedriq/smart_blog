from rest_framework import viewsets

from api.auth.permissions import IsOwnerOrReadOnly
from apps.blogs.models import Article, Blog

from .serializers import ArticlesSerializer, BlogsSerializer


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
