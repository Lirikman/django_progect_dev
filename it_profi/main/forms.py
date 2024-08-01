from django.http import request

from .models import Order, Problem, Article
from django.forms import ModelForm, TextInput, Select, Textarea, HiddenInput


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].queryset = Problem.active_objects.all()

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


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ["problem"]


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Название статьи'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст статьи'
            }),
        }
