from rest_framework import serializers
from django.contrib.auth.models import User
from booking_v2.models import Booking
from datetime import datetime
class SignupSerializer(serializers.ModelSerializer):
    class Meta:

        model=User

        fields=["username","email","password"]
        
class TurfBookingSerializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()
 
    class Meta:

        model=Booking

        fields = "__all__"

        read_only_fields=["id","token_number","appointment_time","created_at"]

        def validate(self,validated_data):

            booking_date=validated_data.get("booking_date")

            turf_id=validated_data.get("turf_id")

            if booking_date<datetime.today().date():

                raise serializers.ValidationError("date should be > cur date")

            last_appointment=Booking.objects.filter(turf_id=turf_id,booking_date=booking_date).last()

            if last_appointment:

                if last_appointment.booking_time == 18:

                    raise serializers.ValidationError("slot full....")

            return validated_data
        


