from rest_framework import serializers

from apps.blogs.models import Article, Blog


class BlogsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    date_of_creation = serializers.CharField(read_only=True)
    
    class Meta:
        model = Blog
        fields = ("title", "description", "owner", "date_of_creation")
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user

        return Blog.objects.create(**validated_data)


class ArticlesSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    publication_date = serializers.CharField(read_only=True)
    
    class Meta:
        model = Article
        fields = ("title", "content", "for_blog", "owner", "publication_date")
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user

        return Article.objects.create(**validated_data)
