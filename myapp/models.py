
from pyexpat import model
from django.db import models


# Create your models here.

class User(models.Model):


    name = models.CharField(max_length=50)
    dob  = models.DateField(max_length=15)
    email = models.EmailField(unique=True)
    mobile  = models.CharField(max_length=15)
    address  = models.TextField(null=True,blank=True)
    password = models.CharField(max_length=15)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.email
