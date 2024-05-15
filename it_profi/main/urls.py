from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('orders', views.orders, name='orders'),
    path('articles', views.articles, name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='single'),
    path('article_upd/<int:pk>', views.ArticleUpdateView.as_view(), name='article_upd'),
    path('article_create', views.ArticleCreateView.as_view(), name='article_create'),
    path('article_del/<int:pk>', views.ArticleDeleteView.as_view(), name='article_del'),

]
