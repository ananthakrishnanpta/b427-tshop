from django.shortcuts import render, redirect 
from django.urls import reverse_lazy

from django.contrib.auth.models import User 

from django.contrib.auth.views import LoginView

from django.views.generic import CreateView

from .forms import UserRegistrationForm, UserLoginForm

class UserRegisterView(CreateView):
    model = User 
    form_class  = UserRegistrationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('signin')

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = UserLoginForm