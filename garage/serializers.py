from .models import Garage
from rest_framework import serializers

class GarageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to serialize
        model = Garage
        # fields to show in json
        fields = ('id', 'make', 'model', 'year', 'grade')