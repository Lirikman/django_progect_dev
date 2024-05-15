from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
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
    order = Order.objects.order_by('id')
    all_id = [x.id for x in Order.objects.all()]
    return render(request, 'main/orders.html', {'orders': order, 'id': all_id})


def articles(request):
    article = Article.objects.all()
    return render(request, 'main/articles.html', {'articles': article})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/single.html'
    context_object_name = 'article'


class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForms
    template_name = 'main/article_upd.html'
    success_url = reverse_lazy('articles')
    success_message = 'Статья успешно обновлена!'


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ArticleForms
    template_name = 'main/article_create.html'
    success_url = reverse_lazy('articles')
    login_url = 'login'
    success_message = 'Статья успешно добавлена!'


class ArticleDeleteView(SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'main/article_del.html'
    success_url = reverse_lazy('articles')
    success_message = 'Статья успешно удалена!'
