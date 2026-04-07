from django.db import models

# Create your models here.
class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField()
    comments = models.CharField(max_length=1000)
    
