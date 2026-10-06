from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


from booking.models import Appointment
from booking.serializers import AppointmentSerializer
# Create your views here.

class AppointmentListCreateviews(APIView):
    def get(self,request):
        qs=Appointment.objects.all()# qs type qs => pynt
        serializer_instance=AppointmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data) 

    def post(self,request):
        form_data=request.data
        serializer_instance=AppointmentSerializer(data=form_data)
        if serializer_instance.is_valid():
                cleaned_data=serializer_instance.validated_data
                turf=cleaned_data.get("turf")
                date=cleaned_data.get("date")

                last_appointment=Appointment.objects.filter(turf=turf,date=date)

                id=0
                if last_appointment:
                     id=last_appointment.booking_id+1
                else:
                    id=1
                print(id,"===============")

                return Response(data={"booking_id":id,"status":"booked"})
        else:
                return Response(data=serializer_instance.errors)

class AppointmentRetrieveUpdateDelete(APIView):

     def get(self,request,pk=None):
        qs=Appointment.objects.filter(id=pk).values()
        t_list = list(qs)
        return Response(data=t_list)
    
     def delete(self,request, pk):
             appointment= Appointment.objects.get(id=pk)
             appointment.delete()

             d_list= {
                "Message": "Deleted successfully"
            }
             return Response(data=d_list)   

     def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=AppointmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Appointment.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

        