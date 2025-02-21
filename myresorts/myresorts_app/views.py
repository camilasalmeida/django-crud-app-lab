from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resort, Trip
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TripForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user
            login(request, user)  # Log the user in
            return redirect('resort-index')
        else:
            error_message = 'Invalid sign up - try again'
            print(form.errors)  # 🔥 Print errors for debugging
    else:
        form = UserCreationForm()  # Empty form for GET request

    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

  


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def resort_index(request):
    resorts = Resort.objects.filter(user=request.user)  # 🔥 Show only user's resorts
    return render(request, 'resorts/index.html', {'resorts': resorts})



@login_required
def resort_detail(request, resort_id):
    resort = Resort.objects.get(id=resort_id)
    if resort.user != request.user:
        return HttpResponse("Unauthorized", status=403)
    trips = resort.trip_set.all().order_by('date')
    trip_form = TripForm()
    return render(request, 'resorts/detail.html', {'resort': resort, 'trips': trips, 'trip_form': trip_form})  

@login_required
def add_trip(request, resort_id):
    form = TripForm(request.POST)
    if form.is_valid():
        new_trip = form.save(commit=False)
        new_trip.resort_id = resort_id
        new_trip.save()
    return redirect('resort-detail', resort_id=resort_id)


class ResortCreate(LoginRequiredMixin, CreateView):
    model = Resort
    fields = ['name', 'country', 'state', 'address', 'lift_ticket']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ResortUpdate(LoginRequiredMixin, UpdateView):
    model = Resort
    fields = ['country', 'state', 'address', 'lift_ticket']


class ResortDelete(LoginRequiredMixin, DeleteView):
    model = Resort
    success_url = '/resorts/'


class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ['date', 'buddy']
    def get_success_url(self):
        trip = self.object 
        return f'/resorts/{trip.resort.id}/'


class TripDelete(LoginRequiredMixin,DeleteView):  
    model = Trip
    template_name = "trips/trip_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resort'] = self.object.resort  
        return context

    def get_success_url(self):
        return f'/resorts/{self.object.resort.id}/'
