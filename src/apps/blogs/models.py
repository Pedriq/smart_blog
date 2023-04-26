from django.db import models
from apps.users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, default=0)


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    for_blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, default=0)


class Rating(models.Model):
    ARTICLE_CHOICES = [
        (1, 'Очень плохо'),
        (2, 'Плохо'),
        (3, 'Средне'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    ]

    article = models.ForeignKey(to=Blog, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(default=0, choices=ARTICLE_CHOICES)
