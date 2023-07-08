from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
