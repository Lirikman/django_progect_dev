from django.test import TestCase
from django.test import Client
from main.models import Article
from users.models import User


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        Article.objects.create(name='article_test', text='text_test')
        User.objects.create_user(username='test', email='test#test.ru', password='123456')

    # Проверка доступности страницы index
    def test_status_index(self):
        response = self.client.get('/index')
        self.assertEqual(200, response.status_code)

    # Проверка доступности страницы article/1
    def test_status_single(self):
        response = self.client.get('/articles/1')
        self.assertEqual(200, response.status_code)

    # Проверка доступа к странице создания статьи без авторизации
    def test_articles(self):
        response = self.client.get('/article_create')
        self.assertEqual(302, response.status_code)

    # Проверка доступа к странице создания статьи для авторизованного пользователя
    def test_status_create_article(self):
        self.client.login(username='test', password='123456')
        response = self.client.get('/article_create')
        self.assertEqual(200, response.status_code)

    # Проверка доступа к странице удаления статьи без авторизации
    def test_status_del_article(self):
        response = self.client.get('/article_del/1')
        self.assertEqual(302, response.status_code)

    # Проверка доступа к странице удаления статьи для авторизованного пользователя
    def test_status_del_article(self):
        self.client.login(username='test', password='123456')
        response = self.client.get('/article_del/1')
        self.assertEqual(200, response.status_code)

    # post запрос
    def test_status_post_article(self):
        self.client.login(username='test', password='123456')
        response = self.client.post('/article_create', {'name': 'article_test'})
        self.assertEqual(200, response.status_code)
