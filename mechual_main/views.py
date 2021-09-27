from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'mechual_main/index.html')

def about(request):
    return render(request, 'mechual_main/about.html')

def contact(request):
    return render(request, 'mechual_main/contact.html')

def events(request):
    return render(request, 'mechual_main/events.html')

def single(request):
    return render(request, 'mechual_main/single.html')