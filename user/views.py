from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


def profile(request, username):
    return HttpResponse(f"Hey! It's profile view!! {username}")


class PasswordChange(PasswordChangeView, SuccessMessageMixin):
    form_class = PasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('main')
    success_message = "you have changed password"


class Register(CreateView, SuccessMessageMixin):
    form_class = SignUpForm
    template_name = 'registration.html'
    success_url = reverse_lazy('main')
    success_message = "you have registered"


class Login(LoginView, SuccessMessageMixin):
    success_url = reverse_lazy('main')
    template_name = 'login.html'
    success_message = "you are login"

    def get_success_url(self):
        return self.success_url


class Logout(LoginRequiredMixin, LogoutView, SuccessMessageMixin):
    next_page = reverse_lazy('main')
    login_url = 'login/'
    success_message = "you are logout"

# Create your views here.
