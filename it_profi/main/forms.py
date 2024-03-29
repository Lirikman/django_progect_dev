from .models import Order, Problem
from django.forms import ModelForm, TextInput, Textarea, Select, ChoiceField


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "phone", "text"]
        widgets = {
            'client': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Введите номер телефона'
            }),
            'text': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите неполадку'
            }),
        }


class ProblemForms(ModelForm):
    class Meta:
        model = Problem
        fields = ["problem"]
        widgets = {
            'problem': TextInput(attrs={
                'class': 'form-control',
                'default': 'Выберите неполадку из списка'
            }),
        }
