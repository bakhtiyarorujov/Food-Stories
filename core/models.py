from django.db import models

# Create your models here.
class Parent(models.Model):
    created_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class AboutUs(Parent):
    about = models.TextField()

class Subscribe(Parent):
    email = models.EmailField(unique=True)

class ContactUs(Parent):
    name = models.CharField(max_length=99)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()