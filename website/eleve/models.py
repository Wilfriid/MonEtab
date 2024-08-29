from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('H', 'Homme'),
        ('F', 'Femme'),
    ]

    SCHOLARSHIP_CHOICES = [
        ('6eme', '6ème'),
        ('5eme', '5ème'),
        ('4eme', '4ème'),
        ('3eme', '3ème'),
        ('2nde', '2nde'),
        ('1ere', '1ère'),
        ('Tle', 'Terminale'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    scholarship = models.CharField(max_length=5, choices=SCHOLARSHIP_CHOICES)
    matricula = models.CharField(max_length=12, default='')

    



