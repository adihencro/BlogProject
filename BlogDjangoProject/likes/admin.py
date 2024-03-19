from django.contrib import admin
from .models import Like


class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'liked_by', 'post_id', 'comment_id']
    class Meta:
        model = Like

admin.site.register(Like, LikeModelAdmin)
