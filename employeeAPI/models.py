from django.db import models
from django.core.validators import MinValueValidator

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.designation} ({self.age})" 

