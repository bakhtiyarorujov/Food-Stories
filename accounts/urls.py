from django.urls import path
from .views import register, login, profile, reset_pass, forget_pass, change_pass


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('reset-password/', reset_pass, name='reset'),
    path('forget-password/', forget_pass, name='forget'),
    path('change-password/', change_pass, name='change'),
]