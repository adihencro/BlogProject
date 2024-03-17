from django.db import models
from users.models import User
from posts.models import Post

class Like(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('liked_by', 'post')  # Ensure only one like per user-post combination
