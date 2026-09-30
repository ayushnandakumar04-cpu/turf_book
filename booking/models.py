from django.db import models
from turf_crud.models import Turf


class Appointment(models.Model):

    customer_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    date = models.DateField()

    booking_id = models.PositiveIntegerField(
        unique=True,
        editable=False,
        null=True
    )

    booking_time = models.TimeField(
        editable=False,
        null=True
    )

    purpose = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.customer_name
# Create your models here.
