from django.core.management.base import BaseCommand
from main.models import Problem


class Command(BaseCommand):
    help = u'Добавление новой неполадки в БД'

    def add_arguments(self, parser):
        parser.add_argument('problem', type=str, help=u'Наименование неполадки')

    def handle(self, *args, **options):
        problem = options['problem']
        try:
            new_problem = Problem.objects.create(problem=problem)
            new_problem.save()
            print('Новая неполадка успешно добавлена в БД!')
        except:
            print('Ошибка при добавлении в БД')
