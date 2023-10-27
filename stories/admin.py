from django.contrib import admin
from .models import (Category,
                     Receipe,
                     StoryCategory,
                     StoryTag,
                     Story,
                     Comment
                     )

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author']
    list_filter = ['title', 'category', 'author']
    list_display_links = ['title', 'category', 'author']


@admin.register(StoryCategory)
class StoryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(StoryTag)
class StoryTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'story', 'comment', 'parent']
    list_filter = ['author', 'story', 'comment', 'parent']
    list_display_links = ['author', 'story']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    list_filter = ['title', 'author', 'category']
    list_display_links = ['title', 'author', 'category']
