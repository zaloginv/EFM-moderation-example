from django.urls import path
from .views import (
    BlogDetailView, BlogListView, BlogCreationView, BlogRedactionView,
    MainView
)

app_name = 'blog-app'

urlpatterns = [
    path(route='blog_list/', view=BlogListView.as_view(), name='blog-list'),
    path(route='blog_detail/<int:pk>/', view=BlogDetailView.as_view(), name='blog-detail'),
    path(route='blog_creation/', view=BlogCreationView.as_view(), name='blog-creation'),
    path(route='blog_redaction/<int:pk>/', view=BlogRedactionView.as_view(), name='blog-redaction'),

    path(route='', view=MainView.as_view(), name='main'),
]
