from django.urls import path
from . import views


#localhost:8000/my_app/
urlpatterns = [
path('',view=views.index, name='index'), #localhost 8000/my_app/
path('contact/', view=views.contact, name='contact') #localhost 8000/my_app/contact


]