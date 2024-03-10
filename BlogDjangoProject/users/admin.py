from django.contrib import admin
from .models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'bio']
    search_fields = ['first_name', 'last_name']
    class Meta:
        model = User

admin.site.register(User, UserModelAdmin)



