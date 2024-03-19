from django.db import models
from users.models import User

class Like(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.IntegerField(default=0)
    comment_id = models.IntegerField(default=0)


    class Meta:
        unique_together = (('liked_by', 'post_id'), ('liked_by', 'comment_id'))



