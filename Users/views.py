from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)
from .models import User, Student
from .forms import StudentSignUpForm, TeacherSignUpForm

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'Users/signup.html')

def login(request):
    return render(request, 'Users/login.html')

class SignUpView(TemplateView):
    template_name = 'Users/signup.html'

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'Users/signup_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'Users/signup_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')