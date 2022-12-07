from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Try Again"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def movies(request):
    return render(request, 'movies.html')

def register(request):
    return render(request, 'register.html')

def theaters(request):
    return render(request, 'theaters.html')

def checkout(request):
    return render(request, 'checkout.html')