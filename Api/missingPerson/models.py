from django.db import models

# Create your models here.
class MissingPerson (models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    STATUS_CHOICES = [
        ('missing', 'Missing'),
        ('found', 'Found')
    ]
    
    firstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
