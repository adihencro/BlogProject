from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from users.models import User

    
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE) #when user deleted all his posts will be deleted as well

    
    def __str__(self):
        return self.title