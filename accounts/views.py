from django.shortcuts import render, redirect
from django.views.generic import FormView,UpdateView
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from  django.urls import reverse_lazy
# Create your views here.

class UserRegistrationView(FormView):
    template_name='accounts/user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')

    def form_valid(self, form):
        user=form.save()
        login( self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name="accounts/lgoin.html"
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserUpdateView(UpdateView):
    model=User
    form_class=UserUpdateForm
    template_name='accounts/profile.html'
    success_url=reverse_lazy('home')
    pk_url_kwarg='id'