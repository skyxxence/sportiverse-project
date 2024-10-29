from django.urls import path
from .views import share_content
urlpatterns = [ 
    path('content/', share_content)
]