from django.urls import path, include
from blogging.views import stub_view, list_view, detail_view, PostViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', stub_view, name="blog_index"),
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
