from django.core.management.base import BaseCommand
from main.models import Article
from faker import Faker


class Command(BaseCommand):
    help = u'Генерация фейковых статей в БД'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help=u'Количество статей')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        try:
            for i in range(count):
                fake = Faker('ru_RU')
                fake_name = fake.text()[:20]
#                fake_image = fake.image()
                fake_text = fake.text()
                fake_source = fake.uri()
                Article.objects.create(name=fake_name, text=fake_text, source=fake_source)
            print('Фэйковые статьи успешно добавлены в БД!')
        except:
            print('Ошибка при добавлении в БД')