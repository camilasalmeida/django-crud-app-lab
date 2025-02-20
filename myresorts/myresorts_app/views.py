from django.shortcuts import render
from django.http import HttpResponse


class Resort:
    def __init__(self, name, country, state, address, lift_ticket):
        self.name = name
        self.country = country
        self.state = state
        self.address = address
        self.lift_ticket = lift_ticket

resorts = [
    Resort("Aspen Snowmass", "USA", "Colorado", "Aspen, CO 81611", "Ikon Pass"),
    Resort("Whistler Blackcomb", "Canada", "British Columbia", "Whistler, BC V8E 0X9", "Epic Pass"),
    Resort("Zermatt", "Switzerland", "Valais", "Bahnhofstrasse 55, 3920 Zermatt", "Day Lift Ticket"),
    Resort("Chamonix", "France", "Haute-Savoie", "35 Place de la Mer de Glace, 74400 Chamonix", "Day Lift Ticket"),
    Resort("Cerro Catedral", "Argentina", "Río Negro", "San Carlos de Bariloche, Río Negro", "Day Lift Ticket"),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resort_index(request):
    return render(request, 'resorts/index.html', {'resorts': resorts})