from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    link = models.URLField(max_length=500)
    category = models.CharField(max_length=200, blank=True)
    photo_main = models.ImageField(upload_to='photos')
    photo_1 = models.ImageField(upload_to='photos', blank=True)
    photo_2 = models.ImageField(upload_to='photos', blank=True)
    photo_3 = models.ImageField(upload_to='photos', blank=True)
    photo_4 = models.ImageField(upload_to='photos', blank=True)
    is_published = models.BooleanField(default=True)

def __str__(self):
    return self.title