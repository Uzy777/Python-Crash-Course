"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all posts.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single blog.
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    # Page for adding a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new entry.
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Page for editing an entry.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]