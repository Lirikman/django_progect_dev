from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Order, Article
from .forms import OrderForm, ArticleForms
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView


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
            messages.success(request, 'Заявка успешно создана! Ожидайте звонка мастера!')
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
    return render(request, 'main/orders.html', {'orders': order})


def articles(request):
    article = Article.objects.all()
    return render(request, 'main/articles.html', {'articles': article})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/single.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForms
    template_name = 'main/article_upd.html'
    success_url = reverse_lazy('articles')


class ArticleCreateView(CreateView):
    form_class = ArticleForms
    template_name = 'main/article_create.html'
    success_url = reverse_lazy('articles')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'main/article_del.html'
    success_url = reverse_lazy('articles')
