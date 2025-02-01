from django.db import models
from django.utils import timezone

# Cleaner Model
class Cleaner(models.Model):
    Name = models.CharField(max_length=100)
    Phone_no = models.CharField(max_length=15, null=True, blank=True)
    Gender = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)
    Role = models.CharField(max_length=15)
    Email = models.EmailField(null=True, blank=True,unique=True)
    Password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.Name}"

# Task Model
class Task(models.Model):
 Description = models.TextField(null=True, blank=True)
 Status = models.CharField(max_length=100)  
 Date = models.DateTimeField(auto_now_add=True)
 location = models.CharField(max_length=100)
 task_name = models.CharField(max_length=100)
 cleaner=models.ForeignKey(Cleaner, on_delete=models.CASCADE,null=True)

 def __str__(self):
        return f"{self.task_name}"



class Admin(models.Model):
    email = models.EmailField(null=True, blank=True,unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.email}"
