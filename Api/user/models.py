from django.db import models

# Create your models here.
class User(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed')
    ]

    firstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    locaton = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
