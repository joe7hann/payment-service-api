from .models import ExpiredPayment
from .serializers import ExpiredPaymentSerializer
from rest_framework import viewsets , permissions, status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# class ExpiredPaymentViewSet(viewsets.ModelViewSet):
#     queryset = ExpiredPayment.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ExpiredPaymentSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request, *args, **kwargs):
#         # Do something with the request data
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ExpiredPaymentViewSet(viewsets.ViewSet):
    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


