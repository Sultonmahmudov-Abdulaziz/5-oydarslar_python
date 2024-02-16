from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render



def about(request):
    return render(request,template_name= 'student/about.html')

def contact(request):
    return render(request,template_name= 'student/contact.html')

def index(request):
    return render(request,template_name= 'student/index.html')

def homepage(request):
    return render(request,template_name= 'student/homepage.html')


