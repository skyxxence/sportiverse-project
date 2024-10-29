from django.urls import path
from .views import send_tweet
urlpatterns = [
    path('message/', send_tweet)
]