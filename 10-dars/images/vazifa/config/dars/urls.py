from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('homepage/',views.homepage, name='homepage'),
]

