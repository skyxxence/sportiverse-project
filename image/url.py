from .views import image_upload
from django.urls import path

urlpatterns = [
    path('upload/', image_upload)
]