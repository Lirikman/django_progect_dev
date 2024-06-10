from datetime import datetime

from dateutil.tz import tz
from django.db import models
from django.urls import reverse


class Problem(models.Model):
    problem = models.TextField('Проблема, неполадка ПК', max_length=30)

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Проблемы и неисправности ПК'


class Order(models.Model):
    client = models.CharField('Клиент', max_length=40)
    phone = models.CharField('Номер телефона', max_length=12)
    text = models.ForeignKey(Problem, on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Дата заказа', default=datetime.now)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'


class Article(models.Model):
    name = models.CharField('Название статьи', max_length=50)
    image = models.ImageField('Изображение', blank=True, null=True, upload_to='main', default='main/info.jpg')
    text = models.TextField('Текст статьи')
    source = models.CharField('Источник', max_length=50)
    date = models.DateTimeField('Дата публикации', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'