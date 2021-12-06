from django.shortcuts import render
from .models import Story

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def sign(request):
    return render(request, 'main/sign.html')

def register(request):
    return render(request, 'main/registration.html')

def story(request):
    story = Story.objects.all()
    return render(request, 'main/story.html', {'story': story})