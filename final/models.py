from django.db import models
from django.urls import reverse



class weight_sweet(models.Model):
    product_name = models.CharField(max_length=64, verbose_name = 'Название весового')
    product_photo = models.ImageField(default='', upload_to='weight_product', verbose_name = 'Фото пряника')
    product_slug = models.SlugField(unique=True, max_length=64, verbose_name = 'ссылка на страницу(ломанный анг.язык)')


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_link", kwargs={"product_slug": self.product_slug})


class single_sweet(models.Model):
    single_product_name = models.CharField(max_length=64, verbose_name = 'Название штучного пряника')
    single_product_photo = models.ImageField(default='', upload_to='single_product', verbose_name = 'фото пряника')
    single_product_price = models.PositiveIntegerField(default=50, verbose_name = 'цена за 1 пряник')
    single_product_slug = models.SlugField(unique=True, max_length=64, verbose_name = 'ссылка на страницу(ломанный анг.язык)')


    def __str__(self):
        return self.single_product_name

    def get_absolute_url(self):
        return reverse("single_product_link", kwargs={"single_product_slug": self.single_product_slug})