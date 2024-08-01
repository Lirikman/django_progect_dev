from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Order, Article
from .forms import OrderForm, ArticleForm
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView


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
    order = Order.active_objects.select_related('text').order_by('id')
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        order = paginator.page(1)
    except EmptyPage:
        order = paginator.page(paginator.num_pages)
    return render(request, 'main/orders.html', {'orders': order})


class ArticleListView(ListView):
    model = Article
    template_name = 'main/articles.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        return Article.active_objects.select_related('user').all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/single.html'
    context_object_name = 'article'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main/article_upd.html'
    success_url = reverse_lazy('articles')
    success_message = 'Статья успешно обновлена!'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    template_name = 'main/article_create.html'
    success_url = reverse_lazy('articles')
    login_url = 'login'
    success_message = 'Статья будет добавлена на сайт после проверки Администратором!'

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'main/article_del.html'
    success_url = reverse_lazy('articles')
    login_url = 'login'
    success_message = 'Статья успешно удалена!'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
