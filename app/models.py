from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Task(models.Model):
    task_tittle=models.CharField(max_length=30)
    task_des=models.TextField()
    task_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_tittle

