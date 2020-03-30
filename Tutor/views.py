from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView
)

# Create your views here.
class HomeView(ListView):
    template_name = "Tutor/Home.html"
    context_object_name = 'home'
    queryset = []




class SignUpView(CreateView): # new
    template_name = 'Tutor/singup.html'
    context_object_name = 'signup'
    queryset = []