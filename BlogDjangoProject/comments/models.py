from django.db import models
from users.models import User
from posts.models import Post

    
class Comment(models.Model):
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.content