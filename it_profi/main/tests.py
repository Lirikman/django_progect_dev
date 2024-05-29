from django.test import TestCase

# Create your tests here.
class TestMain(TestCase):

    # Проверка доступности страницы index
    def test_index(self):
        response = self.client.get('/index')
        self.assertEqual(response.status_code, 200)

    # Проверка переадресации на страницу авторизации
    def test_articles(self):
        response = self.client.get('/article_create')
        self.assertEqual(response.status_code, 302)
