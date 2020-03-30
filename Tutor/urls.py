from django.urls import path, include
from .views import (
    HomeView, SignUpView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    
    
]