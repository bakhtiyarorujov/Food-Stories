from django.db import models

# Create your models here.
class Parent(models.Model):
    created_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class AboutUs(Parent):
    title = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class Subscribe(Parent):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email


class ContactUs(Parent):
    name = models.CharField(max_length=99)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.subject}'
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'