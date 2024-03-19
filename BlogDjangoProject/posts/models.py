from django.db import models
from users.models import User
from likes.models import Like
from django.contrib.contenttypes.fields import GenericRelation

    
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, related_name='posts')

    
    def __str__(self):
        return self.title