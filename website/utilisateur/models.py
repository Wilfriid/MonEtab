from django.db import models

# Create your models here.
class User(models.Model):
    pseudo_name = models.CharField(max_length=15)
    password = models.CharField(max_length=225)
    creat_at = models.DateTimeField(auto_now_add=True)