from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    sub = models.CharField(max_length=10)
    hobbie = models.CharField(max_length=15)