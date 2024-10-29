from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    # print(request.method)
    context ={}
    if request.method == 'POST':
        # print('post request')
       
        username = request.POST['username'].lower()
        password = request.POST['password']
        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            messages.error(request, 'Username already existss.')
            messages.error(request, 'message two.')
            context = {'error' : 'you already have an account'}
            
            
        else:
            first_name = request.POST['First_name']
            messages.success(request, 'successful registration.')
            context = {'success' : 'registration successful, proceed to log in'}
            user = User.objects.create_user(username=username, password=password, first_name=first_name)
            return redirect('go-login')
          
                    
        # print(request.POST)
        # print(username, first_name, password)
        
                         
    return render(request, "register.html", context)

#for login view
def login_view(request):
    context ={}
    if request.method == 'POST':
        # print('post request')
       
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        existing_user = User.objects.filter(username=username).exists()
        
        if not existing_user:
            
            context = {"error" : "you don't have an account, proceed to register "}
            
            
        else:
            user = authenticate(request, username=username, password = password)
            
            if user is not None:
                # print('correct password')
                login(request, user)
                return redirect('go-home')
            else:
                context = {'error': 'oh no!, incorrect password'}
                # print("incorrect password")
            
            
                    
    return render(request, "login.html", context)

def home_view(request):
    return render(request, 'home.html')

# Create your views here.
