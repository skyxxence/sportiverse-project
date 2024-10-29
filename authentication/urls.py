from django.urls import path
from .views import register, login_view, home_view

urlpatterns = [
    
    path('register/', register, name = 'go-register'),
    path('login/', login_view, name='go-login'),
    path('home/', home_view, name= 'go-home'),
]
