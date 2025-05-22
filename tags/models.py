from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='укажите названия тега')
    
    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Укажите прадукт')
    tags = models.ManyToManyField(Tag)
        

    def __str__(self):
        return self.product_name

