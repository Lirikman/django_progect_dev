from datetime import datetime
from django.db import models


class Problem(models.Model):
    problem = models.TextField('Проблема, неполадка ПК', max_length=30)

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Проблемы и неисправности ПК'


class Order(models.Model):
    client = models.CharField('Клиент', max_length=35)
    phone = models.CharField('Номер телефона', max_length=12)
    text = models.ForeignKey(Problem, on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Дата заказа', default=datetime.now)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'
