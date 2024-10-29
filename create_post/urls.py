from django.urls import path
from .views import create_post, get_blog, getAllBlogs
urlpatterns = [ 
    path('post/', create_post, name= 'create-blog'),
    path('view/<int:blog_id>', get_blog, name= 'get-blog'),
    path('all-blogs/', getAllBlogs, name= 'get-all'),
]