from django.contrib import admin
from .models import Like


class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'post', 'liked_by']
    class Meta:
        model = Like

admin.site.register(Like, LikeModelAdmin)
