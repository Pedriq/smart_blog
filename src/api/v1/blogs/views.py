from rest_framework import viewsets

from api.auth.permissions import IsOwner_or_IsStaff_or_ReadOnly
from apps.blogs.models import Article, Blog

from .serializers import ArticlesSerializer, BlogsSerializer


class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = (IsOwner_or_IsStaff_or_ReadOnly, )


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwner_or_IsStaff_or_ReadOnly, )
