from django.core.management.base import BaseCommand

from main.models import Order


# Посмотреть все заявки
class Command(BaseCommand):
    def handle(self, *args, **option):
        order = Order.objects.order_by('id')
        if len(order) > 0:
            for el in order:
                print(str(el.id) + ' - ' + str(el.client) + ' - ' + str(el.phone) + ' - ' + str(el.text))
        else:
            print('Заявки в БД отсутствуют!')
