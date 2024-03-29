from django.db import models


class Problem(models.Model):
    problem = models.CharField('Проблема, неполадка ПК', max_length=100)

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Проблемы и неисправности ПК'


class Order(models.Model):
    client = models.CharField('Клиент', max_length=100)
    phone = models.CharField('Номер телефона', max_length=12)
    text = models.ForeignKey(Problem, on_delete=models.CASCADE)
#    text = models.TextField('Описание проблемы')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'



