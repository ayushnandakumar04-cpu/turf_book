from rest_framework.views import APIView
from django.contrib.auth.models import User
from booking_v2.serializers import SignupSerializer,TurfBookingSerializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
from booking_v2.models import Booking
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from datetime import time,datetime,timedelta
class SignupRegisterview(APIView):
    def post(sef,request):

        form_data=request.data

        serializer_instance=SignupSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            user_object=User.objects.create_user(**cleaned_data)

            ser_inst=SignupSerializer(user_object)

            return Response(data=ser_inst.data)
        
        else:

            return Response(data=ser_inst.errors)


class AppointmentListCreateview(APIView):

    def get(self,request):

        qs=Booking.objects.all()

        serializer=TurfBookingSerializer(qs,many=True)

        return Response(data=serializer.data)
    
    def post(self,request):
        
        form_data = request.data

        serializer_instant = TurfBookingSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            turf_id = cleaned_data.get("turf_id")

            booking_date = cleaned_data.get("booking_date")

            

            last_booking_object = Booking.objects.filter(turf=turf_id,booking_date=booking_date).order_by("booking_time").order_by("booking_time")

            if not last_booking_object.exists():
                 booking_time_details = time(10, 0)

            elif last_booking_object.count() == 1:
                  booking_time_details = time(12, 0)

            else:
                return Response(
                    {"Message": "No booking slots available for this date."}
                )

            
            qs = Booking.objects.create(
                    **cleaned_data,
                    booking_time=booking_time_details
                )

            serializer_instance = TurfBookingSerializer(qs)

            return Response(data=serializer_instance.data)

        else:
           return Response(data=serializer_instant.errors)
     

class AppointmentRetrieveUpdateDeleteView(RetrieveAPIView,DestroyAPIView,UpdateAPIView):

     authentication_classes=[authentication.BasicAuthentication]

     permission_classes=[permissions.IsAuthenticated]

     serializer_class=TurfBookingSerializer

     queryset=Booking.objects.all()
            