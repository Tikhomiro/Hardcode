from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    # Дополнительные поля пользователя

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    # Дополнительные поля продукта

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    # Дополнительные поля урока

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    # Дополнительные поля группы
