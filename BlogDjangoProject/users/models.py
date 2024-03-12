from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=120)
    

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name} {self.email} {self.bio}"


    
