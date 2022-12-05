from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request=request, template_name='my_app/index.html') 


def contact(request):
    return HttpResponse('<h1 style="color: blue; background: black;">This is the contact page</h1>')