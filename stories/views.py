from django.shortcuts import render
from .models import (Category,
                     Receipe,
                     StoryCategory,
                     StoryTag,
                     Story,
                     Comment)

# Create your views here.
def story_list(request):
    stories = Story.objects.all()
    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context=context)

def story_detail(request):
    return render(request, 'single.html')

def recipe_list(request):
    return render(request, 'recipes.html')

def create_story(request):
    return render(request, 'create_story.html')