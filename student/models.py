from datetime import datetime

from django.db import models
# Create your models here.
class contact_us(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100, default='Not available' )
    message = models.CharField(max_length=2000)

