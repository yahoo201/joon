from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request):
    return render(request, 'count.html')

def about(request):
    return render(request, 'about.html')