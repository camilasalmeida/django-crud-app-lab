from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resort, Trip
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TripForm
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resort_index(request):
    resorts = Resort.objects.all()
    return render(request, 'resorts/index.html', {'resorts': resorts})

def resort_detail(request, resort_id):
    resort = Resort.objects.get(id=resort_id)
    trips = resort.trip_set.all().order_by('date')
    trip_form = TripForm()
    return render(request, 'resorts/detail.html', {'resort': resort, 'trips': trips, 'trip_form': trip_form})  

def add_trip(request, resort_id):
    form = TripForm(request.POST)
    if form.is_valid():
        new_trip = form.save(commit=False)
        new_trip.resort_id = resort_id
        new_trip.save()
    return redirect('resort-detail', resort_id=resort_id)


class ResortCreate(CreateView):
    model = Resort
    fields = '__all__'
    success_url = '/resorts/'

class ResortUpdate(UpdateView):
    model = Resort
    fields = ['country', 'state', 'address', 'lift_ticket']


class ResortDelete(DeleteView):
    model = Resort
    success_url = '/resorts/'


class TripUpdate(UpdateView):
    model = Trip
    fields = ['date', 'buddy']
    def get_success_url(self):
        trip = self.object 
        return f'/resorts/{trip.resort.id}/'


class TripDelete(DeleteView):  
    model = Trip
    template_name = "trips/trip_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resort'] = self.object.resort  
        return context

    def get_success_url(self):
        return f'/resorts/{self.object.resort.id}/'
