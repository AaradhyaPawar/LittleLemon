from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    class Meta:
        ordering = ['booking_date']
    
    def __str__(self):
        return f'{self.name} for {self.no_of_guests} guests on {self.booking_date}'
