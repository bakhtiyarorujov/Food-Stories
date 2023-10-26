from django.urls import path
from .views import home, about, contact, email

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('email-subscribers/', email, name='email'),
]