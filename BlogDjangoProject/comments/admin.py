from django.contrib import admin
from .models import Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'updated', 'timestamp', 'post', 'comment_by']
    list_filter = ["updated", "timestamp"]
    class Meta:
        model = Comment

admin.site.register(Comment, CommentModelAdmin)
