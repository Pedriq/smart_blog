from rest_framework import serializers
from apps.blogs.models import Blog, Article


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("title", "description", "owner",)


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content", "for_blog", "owner",)
