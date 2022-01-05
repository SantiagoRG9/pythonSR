from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

class Type(models.Model):

    names = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.names

class Category(models.Model):

    names = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.names

class Employee(models.Model):

    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=150, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateTimeField(auto_now=True, verbose_name="")
    date_update = models.DateTimeField(auto_now_add=True, verbose_name="")
    age = models.IntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names



