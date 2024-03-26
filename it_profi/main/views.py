from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные заполнены некорректно'
    form = OrderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def orders(request):
    order = Order.objects.order_by('-id')
    return render(request, 'main/orders.html', {'title': 'Все заявки', 'orders': order})