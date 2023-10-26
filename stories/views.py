from django.shortcuts import render

# Create your views here.
def story_list(request):
    return render(request, 'stories.html')

def story_detail(request):
    return render(request, 'single.html')

def recipe_list(request):
    return render(request, 'recipes.html')

def create_story(request):
    return render(request, 'create_story.html')