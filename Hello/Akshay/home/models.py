from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=150)
    lastname =models.CharField(max_length=150)
    email =models.CharField(max_length=150)
    City =models.CharField(max_length=150)
    State =models.CharField(max_length=150)
    Pin =models.CharField(max_length=150)
    Phone =models.CharField(max_length=15)
    Date = models.DateField()


