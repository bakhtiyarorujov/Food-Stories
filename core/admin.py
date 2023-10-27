from django.contrib import admin
from .models import (AboutUs,
                     Subscribe,
                     ContactUs) 

# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


@admin.register(Subscribe)
class Subscribe(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']
    list_filter = ['name', 'subject', 'email']
