from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def contact(request):
    return render(request, 'base/contact.html')

def projects(request):
    return render(request, 'base/projects.html')

def resume(request):
    return render(request, 'base/resume.html')
