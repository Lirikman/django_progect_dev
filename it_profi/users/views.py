from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import RegistrationUserForm, UserLoginForm


# Create your views here.
class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    next_page = 'home'
    success_message = 'Добро пожаловать на сайт!'


class UserCreateView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('home')
    success_message = 'Вы успешно зарегистрировались на сайте!'


class UserLogoutView(LogoutView):
    next_page = 'home'
