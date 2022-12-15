from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from .models import Movie
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

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logged Out!"))
    return redirect('home')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def movies(request):
    movie_list = [
        Movie.objects.get(id=1),
        Movie.objects.get(id=2),
        Movie.objects.get(id=3)
    ]
    return render(request, 'movies.html', {'movie_list':movie_list})


def theaters(request):
    return render(request, 'theaters.html')



def checkout(request):
    # Initialize the ticket prices
    kids_price = 5
    adults_price = 10
    seniors_price = 8

    # If this is a POST request (i.e. the user has submitted the form),
    # calculate the total cost of the tickets based on the number of
    # tickets of each type that the user selected
    if request.method == 'POST':
        # Get the number of tickets of each type from the form data
        num_kids = int(request.POST.get('num_kids', 0))
        num_adults = int(request.POST.get('num_adults', 0))
        num_seniors = int(request.POST.get('num_seniors', 0))

        # Calculate the total cost of the tickets
        total_cost = (num_kids * kids_price) + (num_adults * adults_price) + (num_seniors * seniors_price)

        # Render the confirmation page with the total cost and other relevant information
        return render(request, 'confirmation.html', {
            'total_cost': total_cost,
            'num_kids': num_kids,
            'num_adults': num_adults,
            'num_seniors': num_seniors,
        })

    # If this is a GET request (i.e. the user is accessing the page for the first time),
    # simply render the checkout page template
    else:
        return render(request, 'checkout.html')