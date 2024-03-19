from django.db import models
from users.models import User
from posts.models import Post
from likes.models import Like
from django.contrib.contenttypes.fields import GenericRelation

    
class Comment(models.Model):
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, related_name='comments')
    
    def __str__(self):
        return self.content