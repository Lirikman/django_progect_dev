from django.test import TestCase


# Create your tests here.
class TestUrlsCase(TestCase):

    # Проверка доступности страницы index
    def test_index(self):
        response = self.client.get('/index')
        self.assertEqual(200, response.status_code)

    # Проверка переадресации на страницу авторизации
    def test_articles(self):
        response = self.client.get('/article_create')
        self.assertEqual(302, response.status_code)

