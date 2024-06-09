from django.test import TestCase
from main.models import Article, Order
from faker import Faker
from mixer.backend.django import mixer


class TestModelsCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создание тестовой записи в БД и сохранение в качестве переменной класса
        cls.article_1 = Article.objects.create(name='article_1', text='text_test')
        cls.article_2 = Article.objects.create(name='article_2', text='text_test')

    # Проверка корректности количества записей при добавлении в БД
    def test_articles_count(self):
        self.assertEqual(Article.objects.count(), 2)

    # Проверка совпадения Verbose_name поля name с ожидаемым
    def test_name_label(self):
        art = TestModelsCase.article_1
        verbose = art._meta.get_field('name').verbose_name
        self.assertEqual(verbose, 'Название статьи')

    # Проверка совпадения Verbose_name поля text с ожидаемым
    def test_text_label(self):
        art = TestModelsCase.article_1
        verbose = art._meta.get_field('text').verbose_name
        self.assertEqual(verbose, 'Текст статьи')


class TestModels_Faker(TestCase):
    def setUp(self):
        data_generator = Faker(['ru_RU'])
        self.test_name = data_generator.name()
        self.article_test = Article.objects.create(name=self.test_name, text=data_generator.text())

    def test_model_str(self):
        self.assertEqual(str(self.article_test), self.test_name)


class TestModels_Mixer(TestCase):
    def setUp(self):
        self.test_order = mixer.blend(Order, client='Тестов Тест Тестович')

    def test_model_str(self):
        self.assertEqual(self.test_order.client, 'Тестов Тест Тестович')