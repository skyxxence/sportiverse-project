from django.shortcuts import render
from django.http import HttpResponse
from .models import Content

def share_content(request):
    
    print("I am sharing a new content")
    return HttpResponse('welcome to share/content view')

# Create your views here.
