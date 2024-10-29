from django.shortcuts import render
from django.http import HttpResponse
from .models import Quoting

def quote_message(request):
    print("A special quote app")
    return HttpResponse('welcome to quote/message views')




# Create your views here.
