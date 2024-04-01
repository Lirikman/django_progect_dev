from django.core.management.base import BaseCommand
from main.models import Order


#  Удалить заявку
class Command(BaseCommand):
    help = u'Удаление записи из БД'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help=u'Номер удаляемой записи!')

    def handle(self, *args, **options):
        num = options['num']
        try:
            order = Order.objects.get(id=num)
            order.delete()
            print('Запись успешно удалена из БД!')
        except:
            print('Данной записи не существует!')
