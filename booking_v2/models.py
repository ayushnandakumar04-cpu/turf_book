from django.db import models
class Turf(models.Model):

    name = models.CharField(max_length=200)

    date=models.DateField()

    location = models.CharField(max_length=200)

    email = models.EmailField()

    phone_number = models.PositiveIntegerField()

    duration = models.TimeField()

    end_duration = models.TimeField()

    def __str__(self,name):

        return self.name