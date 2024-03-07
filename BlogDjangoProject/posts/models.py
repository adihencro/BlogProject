from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=120)
    

    def __str__(self):
        return f"{self.first_name} ({self.last_name} {self.email} {self.bio})"
    

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE) #when user deleted all his posts will be deleted as well

    
    def __str__(self):
        return self.title