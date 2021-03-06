# Generated by Django 2.2.1 on 2019-06-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status_delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status_payment',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_process', 'Обрабатывается'), ('shipped', 'Отправлен'), ('ready_to_pickup', 'Готов к самовывозу'), ('completed', 'Завершён')], default='in_process', max_length=250, verbose_name='Статус доставки'),
        ),
    ]
