from .views import quote_message
from django.urls import path
urlpatterns = [
    path('message/', quote_message)
] 