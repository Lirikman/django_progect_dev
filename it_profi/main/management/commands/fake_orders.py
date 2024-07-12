from django.core.management.base import BaseCommand
from main.models import Order, Problem
from faker import Faker


class Command(BaseCommand):
    help = u'Генерация фейковых заявок в БД'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help=u'Количество заявок')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        try:
            for i in range(count):
                fake = Faker('ru_RU')
                fake_name = fake.name()
                fake_phone = fake.phone_number()
                random_problem = Problem.active_objects.order_by('?').first()
                Order.objects.create(client=fake_name, phone=fake_phone, text=random_problem)
            print('Фэйковые заявки успешно добавлена в БД!')
        except:
            print('Ошибка при добавлении в БД')
