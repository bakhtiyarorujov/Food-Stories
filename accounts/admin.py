from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username', 'date_joined', 'is_active', 'is_staff']
    list_filter = ['first_name', 'last_name', 'email', 'username', 'date_joined', 'is_active', 'is_staff']
    list_display_links = ['first_name', 'last_name', 'email', 'username']