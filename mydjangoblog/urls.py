from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentCreateView

urlpatterns = [
    # path('', views.index, name='index'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='new_comment'),
    path('', BlogListView.as_view(), name='home'),
    
    
]
