from django.db import models

# Create your models here.
class Turf(models.Model):

    name = models.CharField(max_length=200)

    TURF_TYPE_OPTIONS = (

        ("football", "Football"),
        ("cricket", "Cricket"),
        ("basketball", "Basketball"),
        ("badminton", "Badminton"),
        ("tennis", "Tennis"),
        ("volleyball", "Volleyball"),
        ("other", "Other")
    )

    turf_type = models.CharField(
        max_length=200,
        choices=TURF_TYPE_OPTIONS,
        default="other"
    )

    location = models.CharField(max_length=200)

    price = models.PositiveIntegerField()

    contact_email = models.EmailField(unique=True)

    end_time=models.TimeField()

    # String representation of object
    def __str__(self):

        return self.name