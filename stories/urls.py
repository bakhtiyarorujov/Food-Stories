from django.urls import path
from .views import story_list, story_detail, recipe_list, create_story


urlpatterns = [
    path('stories/', story_list, name = 'story_list'),
    path('story/', story_detail, name='story_detail'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('create-story/', create_story, name='create_story'),
]