from turtle import title
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=250)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering=['complete']

# Create your models here.
