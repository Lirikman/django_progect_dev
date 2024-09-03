from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from .views_api import ArticleApiView, ProblemApiView, ClientsApiView, OrdersApiView

router = routers.DefaultRouter()
router.register('article', ArticleApiView)
router.register('problem', ProblemApiView)
router.register('order', OrdersApiView)
router.register('clients', ClientsApiView)


urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('orders', views.orders, name='orders'),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='single'),
    path('article_upd/<int:pk>', views.ArticleUpdateView.as_view(), name='article_upd'),
    path('article_create', views.ArticleCreateView.as_view(), name='article_create'),
    path('article_del/<int:pk>', views.ArticleDeleteView.as_view(), name='article_del'),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
