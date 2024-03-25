from django.db import models


class Order(models.Model):
    client = models.CharField('Клиент', max_length=100)
    phone = models.CharField('Номер телефона', max_length=12)
    text = models.TextField('Описание проблемы')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'