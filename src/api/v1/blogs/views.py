from rest_framework import viewsets
from apps.blogs.models import Blog, Article
from .serializers import BlogsSerializer, ArticlesSerializer


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
