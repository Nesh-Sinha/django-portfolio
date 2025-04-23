from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'portfolio/base.html')

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def projects(request):
    return render(request, 'portfolio/projects.html')
