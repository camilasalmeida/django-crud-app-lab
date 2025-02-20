from django.shortcuts import render
from django.http import HttpResponse
from .models import Resort
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class ResortCreate(CreateView):
    model = Resort
    fields = '__all__'
    success_url = '/resorts/'

class ResortUpdate(UpdateView):
    model = Resort
    fields = ['country', 'state', 'address', 'lift_ticket']
    # template_name = 'resorts/resort_form.html'

class ResortDelete(DeleteView):
    model = Resort
    success_url = '/resorts/'
    # template_name = 'resorts/resort_confirm_delete.html'