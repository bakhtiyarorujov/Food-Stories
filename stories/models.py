from django.db import models
from core.models import Parent
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Category(Parent):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Receipe(Parent):
    title = models.CharField(max_length=99)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recipe')
    description = models.TextField()
    photo = models.ImageField(upload_to='media/recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receipe')

    def __str__(self) -> str:
        return self.title


class StoryCategory(Parent):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class StoryTag(Parent):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Story(Parent):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/story')
    description = RichTextField()
    small_description = models.CharField(max_length=155)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story')
    tags = models.ManyToManyField(StoryTag, related_name='story_tag')
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE, related_name='story_category')

    def __str__(self) -> str:
        return self.title


class Comment(Parent):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comment_story')
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_parent')

    def __str__(self) -> str:
        return f'{self.author} - {self.story}'