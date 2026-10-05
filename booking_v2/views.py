from rest_framework.views import APIView
from django.contrib.auth.models import User
from booking_v2.serializers import SignupSerializer,TurfBookingSerializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
from booking_v2.models import Turf
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

class TurfBookingListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.AllowAny]

    def get(self,request):

        qs = Turf.objects.all()

        serializer_instant = TurfBookingSerializer(qs,many=True)

        return Response(data=serializer_instant.data)


    def post(self,request):

        form_data = request.data

        serializer_instant = TurfBookingSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            Turf.objects.create(**cleaned_data)

            return Response(data=serializer_instant.data)

        else:
            
            return Response(data=serializer_instant.errors)

class TurfBokingRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.AllowAny]

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instant = TurfBookingSerializer(qs)

        return Response(data=serializer_instant.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instant = TurfBookingSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            Turf.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instant.data)

    def delete(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instant = TurfBookingSerializer(qs)

        qs.delete()

        return Response(data=serializer_instant.errors)
            