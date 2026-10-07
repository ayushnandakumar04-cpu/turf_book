from django.db import models
from turf_crud.models import Turf
class Booking(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.PositiveIntegerField()

    turf = models.ForeignKey(Turf,
        on_delete=models.CASCADE,
    )

    duration = models.CharField(
        max_length=100
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    def __str__(self):
        return self.name