from .models import Order, Problem
from django.forms import ModelForm, TextInput, Select


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "phone", "text"]
        widgets = {
            'client': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Иванов Иван Иванович'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: +70000000000'
            }),
            'text': Select(attrs={
                'class': 'form-control',
            }),
        }


class ProblemForms(ModelForm):
    class Meta:
        model = Problem
        fields = ["problem"]
