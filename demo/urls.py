from django.urls import path
from .views import PostDetailView, PostListView, TagDetailView

urlpatterns = [
    path('', PostListView.as_view(template_name='post_list.html'), name='post-list'),
    path('<slug>/', PostDetailView.as_view(template_name='post_with_sidebar.html'), name='post-view'),
    path('tag/<slug>/', TagDetailView.as_view(template_name='tag.html'), name='tag-view'),
]
