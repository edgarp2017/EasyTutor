from django.shortcuts import render
from django.views.generic import (
    ListView,
)

# Create your views here.
class HomeView(ListView):
    template_name = "Tutor/Home.html"
    context_object_name = 'home'
    queryset = []