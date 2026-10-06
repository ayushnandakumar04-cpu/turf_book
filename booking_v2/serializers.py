from rest_framework import serializers
from django.contrib.auth.models import User
from booking_v2.models import Turf
from booking.models import Appointment
from datetime import time
class SignupSerializer(serializers.ModelSerializer):
    class Meta:

        model=User

        fields=["username","email","password"]
        
class TurfBookingSerializer(serializers.ModelSerializer):

        duration = serializers.TimeField(
            format="%I:%M %p",
            input_formats=["%I:%M %p"]
        )

        class Meta:

         model = Turf

         fields = "__all__"

        def validate(self,validate_data):

          end_time = validate_data.get("duration")

          if end_time >= time(21, 0):
               
                raise serializers.ValidationError("Turf Closed")

          return validate_data

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:

        model=Appointment

        fields="__all__"

        read_only_fields=["id","duration","email",]

