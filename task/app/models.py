from django.db import models
from django.utils.timezone import now

# Create your models here.

# this the model for events

class Event(models.Model):
    event = models.CharField(max_length=100)
    vanue = models.CharField(max_length=100)
    image = models.ImageField(upload_to='eventImage/') 
    date = models.DateField() 
    evntNum = models.IntegerField(default=True) 

    def __str__(self):
        return self.event 

class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name