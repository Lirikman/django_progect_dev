from django.forms import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован!')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'Придумайте логин'})
            self.fields['email'].widget.attrs.update({'placeholder': 'Введите свой email'})
            self.fields['first_name'].widget.attrs.update({'placeholder': 'Введите Ваше имя'})
            self.fields['last_name'].widget.attrs.update({'placeholder': 'Введите Вашу фамилию'})
            self.fields['password1'].widget.attrs.update({'placeholder': 'Придумайте пароль'})
            self.fields['password2'].widget.attrs.update({'placeholder': 'Повторите пароль'})
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})