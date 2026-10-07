from django.db import models
from turf_crud.models import Turf


class Appointment(models.Model):

    name = models.CharField(max_length=200)

    turf = models.ForeignKey(Turf,
           on_delete=models.CASCADE,
       )
   
    location = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.PositiveIntegerField()