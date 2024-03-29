# Generated by Django 5.0.3 on 2024-03-29 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_problem_alter_order_options_alter_order_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'verbose_name': 'Неисправность', 'verbose_name_plural': 'Проблемы и неисправности ПК'},
        ),
        migrations.AlterField(
            model_name='order',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.problem'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem',
            field=models.CharField(max_length=100, verbose_name='Проблема, неполадка ПК'),
        ),
    ]
