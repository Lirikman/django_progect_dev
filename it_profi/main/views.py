from django.shortcuts import render
from .models import Order
from .forms import OrderForm


def index(request):
    orders = Order.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'orders': orders})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)