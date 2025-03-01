from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Resort(models.Model):
    LIFT_TICKET_CHOICES = [
        ('Ikon Pass', 'Ikon Pass'),
        ('Epic Pass', 'Epic Pass'),
        ('Day Lift Ticket', 'Day Lift Ticket'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  
    address = models.TextField(max_length=250)
    lift_ticket = models.CharField(max_length=20, choices=LIFT_TICKET_CHOICES, default='Day Lift Ticket')
    
    def __str__(self):
        return f"{self.name} ({self.country})"
    
    def get_absolute_url(self):
        return reverse('resort-detail', kwargs={'resort_id': self.id})
    

class Trip(models.Model):
    date = models.DateField()
    buddy = models.CharField(max_length=100)  

    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.buddy} - {self.date}"



