# Generated by Django 2.2.1 on 2019-06-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190608_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='Россия', max_length=250, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, default='123@123.123', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='order',
            name='locality',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='44', max_length=20, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='order',
            name='region',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Итоговая стоимость'),
        ),
    ]