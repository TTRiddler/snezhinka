# Generated by Django 2.2.1 on 2019-06-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20190608_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='materials',
            field=models.CharField(default='', help_text='Пример: Кожа, Хлопок', max_length=250, verbose_name='Материалы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(default='', help_text='Пример: 43, 44', max_length=250, verbose_name='Размеры'),
        ),
    ]