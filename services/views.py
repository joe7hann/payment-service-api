from .models import Service
from .serializers import ServiceSerializer
from rest_framework import viewsets , permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

#class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    #permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = ServiceSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    


