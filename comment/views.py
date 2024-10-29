from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

#FBV(Function based View)

def comment_app(request):
    # print(request)

    print("Write your comment here")
    return HttpResponse('welcome to comment/onpost view')

# Create your views here.
