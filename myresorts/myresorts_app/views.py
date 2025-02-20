from django.shortcuts import render
from django.http import HttpResponse
from .models import Resort

def home(request):
    return render(request, )

def about(request):
    return render(request, 'about.html')

def resort_index(request):
    resorts = Resort.objects.all()
    return render(request, 'resorts/index.html', {'resorts': resorts})

def resort_detail(request, resort_id):
    resort = Resort.objects.get(id=resort_id)
    return render(request, 'resorts/detail.html', {'resort': resort})


