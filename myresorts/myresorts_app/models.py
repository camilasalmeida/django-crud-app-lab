from django.db import models
from django.urls import reverse

class Resort(models.Model):
    LIFT_TICKET_CHOICES = [
        ('Ikon Pass', 'Ikon Pass'),
        ('Epic Pass', 'Epic Pass'),
        ('Day Lift Ticket', 'Day Lift Ticket'),
    ]

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  
    address = models.TextField(max_length=250)
    lift_ticket = models.CharField(max_length=20, choices=LIFT_TICKET_CHOICES, default='Day Lift Ticket')

    def __str__(self):
        return f"{self.name} ({self.country})"
    
    def get_absolute_url(self):
        return reverse('resort-detail', kwargs={'resort_id': self.id})