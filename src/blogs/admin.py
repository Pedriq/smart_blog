from django.contrib import admin

from blogs.models import Article, Blog, Rating


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_creation')
    search_fields = ('title',)
    ordering = ('-title',)


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_blog', 'publication_date')
    search_fields = ('title',)
    ordering = ('-title',)


@admin.register(Rating)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'rating')
    search_fields = ('article',)
    ordering = ('-article',)
