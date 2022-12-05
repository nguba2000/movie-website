from django.urls import path
from . import views


#localhost:8000/second_app/
urlpatterns = [
path('',view=views.index, name='index'), #localhost 8000/second_app/
]