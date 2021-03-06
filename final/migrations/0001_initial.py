# Generated by Django 3.1.5 on 2021-01-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='single_sweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_product_name', models.CharField(max_length=64, verbose_name='Название штучного пряника')),
                ('single_product_photo', models.ImageField(default='', upload_to='single_product', verbose_name='фото пряника')),
                ('single_product_price', models.PositiveIntegerField(default=50, verbose_name='цена за 1 пряник')),
                ('single_product_slug', models.SlugField(max_length=64, unique=True, verbose_name='ссылка на страницу(ломанный анг.язык)')),
            ],
        ),
        migrations.CreateModel(
            name='weight_sweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64, verbose_name='Название весового')),
                ('product_photo', models.ImageField(default='', upload_to='weight_product', verbose_name='Фото пряника')),
                ('product_slug', models.SlugField(max_length=64, unique=True, verbose_name='ссылка на страницу(ломанный анг.язык)')),
            ],
        ),
    ]
