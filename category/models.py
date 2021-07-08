from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    category_description = models.TextField(max_length=200, blank=True)
    category_image = models.ImageField(upload_to='images/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
