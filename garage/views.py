from .models import Garage
from rest_framework import viewsets, permissions
from .serializers import GarageSerializer

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    permission_classes = [permissions.AllowAny]