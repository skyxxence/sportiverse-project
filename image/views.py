from django.shortcuts import render
from .models import ImageFile
from django.http import HttpResponse


def image_upload(request):
    print("select image to upload")
    
    return HttpResponse("welcome to image/upload views")

# Create your views here.
