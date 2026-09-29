from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from turf_crud.models import Turf
# Create your views here.
# superhero,doctor
class TurfListCreateView(APIView):
    def get(self,request):
        qs=Turf.objects.all().values()
        t_list=list(qs)
        return Response(data=t_list)

    def post(self,request):
        form_data=request.data
        Turf.objects.create(
            name=form_data.get("name"),
            turf_type=form_data.get("turf_type"),
            location=form_data.get("location"),
            price=form_data.get("price"),
            contact_email=form_data.get("contact_email")
        )
        return Response(data=
                        {"message":"created"}
                    )

class TurfListRetrieveView(APIView):
    def get(self,request,pk=None):
        qs=Turf.objects.filter(id=pk).values()
        t_list = list(qs)
        return Response(data=t_list)
    
    def delete(self,request, pk):
             turf= Turf.objects.get(id=pk)
             turf.delete()
             t_list= {
                "Message": "Deleted successfully"
            }
             return Response(data=t_list)   

    def put(self,request,pk):
        form_data =(request.data)
        turf= Turf.objects.get(id=pk)
        Turf.objects.create(
                            name=form_data.get("name"),
                            turf_type=form_data.get("turf_type"),
                            location=form_data.get("location"),
                            price=form_data.get("price"),
                            contact_email=form_data.get("contact_email")
                    )
        
        response_data={
                "Message": "Turf booking updated successfully"
            }
        return Response(data=response_data)

    