from django.urls import path
from .views import comment_app
urlpatterns = [ 
    path('onpost/', comment_app)
]