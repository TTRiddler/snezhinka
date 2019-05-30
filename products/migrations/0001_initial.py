# Generated by Django 2.2.1 on 2019-05-29 18:46

from django.db import migrations, models
import django.db.models.deletion
import products.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Заполнится при сохранении', max_length=250, unique=True, verbose_name='Slug')),
                ('seo_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, max_length=250, null=True, verbose_name='Keywords')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=250, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Заполнится при сохранении', max_length=250, unique=True, verbose_name='Slug')),
                ('seo_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, max_length=250, null=True, verbose_name='Keywords')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('vendor_code', models.CharField(max_length=50, verbose_name='Цвет')),
                ('description', tinymce.models.HTMLField(verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Заполнится при сохранении', max_length=250, unique=True, verbose_name='Slug')),
                ('seo_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, max_length=250, null=True, verbose_name='Keywords')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='Категория')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SubCategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_without_sale', models.PositiveIntegerField(default=0, verbose_name='Цена без скидки')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Скидка')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена со скидкой')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='На складе')),
                ('purchased', models.PositiveIntegerField(default=0, verbose_name='Куплено')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='products.ProductMaterial', verbose_name='Материал')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='products.Product', verbose_name='Товар')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='products.ProductSize', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.models.Image.get_picture_url, verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]