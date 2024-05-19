from django.db import models

class Books (models.Model):
    id = models.IntegerField(primary_key=True)
    title= models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    year_of_publish = models.IntegerField()
    
    def __str__(self):
        return self.title
    

# Create your models here.
