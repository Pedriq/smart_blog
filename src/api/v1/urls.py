from rest_framework import routers
from django.urls import path, include
from .blogs.views import BlogsViewSet, ArticlesViewSet


router_for_blog = routers.SimpleRouter()
router_for_blog.register(r'blog', BlogsViewSet)
router_for_article = routers.SimpleRouter()
router_for_article.register(r'article', ArticlesViewSet)

urlpatterns = [
    path('v1/', include(router_for_blog.urls)),
    path('v1/', include(router_for_article.urls)),
]