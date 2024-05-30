from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    


class Task(models.Model):
    
    title   = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    project =models.ForeignKey(Project,related_name='tasks', on_delete=models.CASCADE

)

    def __str__(self):
        return self.title



