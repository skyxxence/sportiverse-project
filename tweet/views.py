from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


def send_tweet(request):
    print("this is a tweet app")
    return HttpResponse('welcome to tweet/message view')

# Create your views here.
