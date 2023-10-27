from django.db import models
from core.models import Parent
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Category(Parent):
    name = models.CharField(max_length=20)

class Receipe(Parent):
    title = models.CharField(max_length=99)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recipe')
    description = models.TextField()
    photo = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receipe')

class StoryCategory(Parent):
    name = models.CharField(max_length=25)

class StoryTag(Parent):
    name = models.CharField(max_length=25)

class Story(Parent):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='story')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story')
    tag = models.ManyToManyField(StoryTag, related_name='story_tag')
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE, related_name='story_category')

class Comment(Parent):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='comment_parent')