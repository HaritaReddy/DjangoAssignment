from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    contact = models.IntegerField()
    address = models.TextField()