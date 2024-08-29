from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    courses = models.CharField(max_length=15)
    number = models.CharField(max_length=10)
    ville = models.CharField(max_length=20)
