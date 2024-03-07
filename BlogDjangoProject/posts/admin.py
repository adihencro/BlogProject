from django.contrib import admin
from .models import *

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'updated', 'timestamp', 'creator']
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'bio']
    search_fields = ['first_name', 'last_name']
    class Meta:
        model = User


admin.site.register(Post, PostModelAdmin)
admin.site.register(User, UserModelAdmin)

