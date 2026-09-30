from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):

    customer_name=serializers.CharField()

    phone=serializers.CharField()

    booking_id = serializers.IntegerField(read_only=True)

    turf=serializers.IntegerField()

    date=serializers.DateField()

    purpose=serializers.CharField()

    booking_time=serializers.TimeField(read_only=True)

    created_at=serializers.DateTimeField(read_only=True)
