from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from users.models import User
from it_profi import settings


class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta():
        abstract = True


class Problem(IsActiveMixin, models.Model):
    problem = models.TextField('Проблема, неполадка ПК', max_length=30)

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Неисправность'
        verbose_name_plural = 'Проблемы и неисправности ПК'


class Order(IsActiveMixin, models.Model):
    client = models.CharField('Клиент', max_length=40)
    phone = models.CharField('Номер телефона', max_length=12)
    problem = models.ForeignKey(Problem, on_delete=models.DO_NOTHING, verbose_name='Неполадка')
    date = models.DateTimeField('Дата заказа', default=datetime.now)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = 'Все заявки'


class Article(IsActiveMixin, models.Model):
    name = models.CharField('Название статьи', max_length=50)
    image = models.ImageField('Изображение', blank=True, null=True, upload_to='main', default='main/info.jpg')
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации', default=datetime.now)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Clients(models.Model):
    client = models.CharField("ФИО клиента", max_length=50)
    phone = models.CharField("Номер телефона клиента", max_length=12)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Все клиенты'


@receiver(post_save, sender=Order)
def add_order(sender, instance, **kwargs):
    Clients.objects.create(client=instance, phone=instance.phone)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
