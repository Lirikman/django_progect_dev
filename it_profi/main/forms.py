from .models import Order
from django.forms import ModelForm, TextInput


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "phone", "text"]
        widgets = {"client": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ФИО'
        }),

        }