from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'user-profile.html')

def change_pass(request):
    return render(request, 'change_password.html')

def forget_pass(request):
    return render(request, 'forget_password.html')

def reset_pass(request):
    return render(request, 'reset_password.html')