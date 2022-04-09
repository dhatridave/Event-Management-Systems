from django.db import models
from pyexpat import model

# Create your models here.


class Event(models.Model):


        ename = models.CharField(max_length=50)
        edescription = models.TextField(max_length=500)
        famount = models.IntegerField()