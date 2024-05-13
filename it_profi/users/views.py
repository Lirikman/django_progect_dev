from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import RegistrationUserForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('main:index')
