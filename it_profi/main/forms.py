from .models import Order
from django.forms import ModelForm, TextInput, Textarea


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
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание проблемы'
            }),
        }
