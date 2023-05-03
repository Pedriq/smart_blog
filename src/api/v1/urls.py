from django.urls import include, path, re_path
from rest_framework import routers

from .blogs.views import ArticlesViewSet, BlogsViewSet

router_for_blog = routers.SimpleRouter()
router_for_blog.register(r'blog', BlogsViewSet)
router_for_article = routers.SimpleRouter()
router_for_article.register(r'article', ArticlesViewSet)

urlpatterns = [
    path('v1/', include(router_for_blog.urls)),
    path('v1/', include(router_for_article.urls)),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^v1/auth/', include('djoser.urls.authtoken')),
]