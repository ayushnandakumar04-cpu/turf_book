from rest_framework import serializers
from turf_crud.models import Turf

class TurfSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)

    name=serializers.CharField()

    turf_type=serializers.ChoiceField(choices=Turf.TURF_TYPE_OPTIONS)

    location=serializers.CharField()

    price=serializers.IntegerField()
    
    contact_email=serializers.EmailField()

    def validate(self,validated_data):
                 
                 price=validated_data.get("price")
     
                 if price<1000:
     
                     raise serializers.ValidationError("invalid price>1000")
                 
                 return validated_data
     
class UserSerializers(serializers.Serializer):
     username=serializers.CharField()
     password=serializers.CharField()
     email=serializers.EmailField()