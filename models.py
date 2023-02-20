from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100, default='Not available' )
    room_no = models.IntegerField()
    
