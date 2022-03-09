from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    memory_ch = [
        ('-', '-'),
        ('64GB', '64GB'),
        ('128GB', '128GB'),
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1TB', '1TB'),
    ]
    name = models.CharField(max_length=255, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=SET_NULL, blank=True, null=True, verbose_name='Категория товара')
    image = models.ImageField(upload_to='media', verbose_name='Картинка товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    color = models.CharField(max_length=255, verbose_name='Цвет товара', blank=True, null=True)
    memory = models.CharField(choices=memory_ch, null=True, default='128GB', max_length=255)
    description = models.TextField()
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    user_img=models.ImageField(upload_to='avatars', null=True, blank=True)
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    name=models.CharField(max_length=50, null=True)
    email=models.CharField(max_length=50, null=True)
    telephone=models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.user)

    
class SendMessage(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    text=models.TextField()

    def __str__(self):
        return str(self.name)
    



    