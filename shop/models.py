from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category)
    description = models.TextField(max_length=500)
    image = models.URLField(max_length=100, default="https:\\")

    def __str__(self):
        return self.name
