from .models import ExpiredPayment
from rest_framework.serializers import ModelSerializer

class ExpiredPaymentSerializer(ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = "__all__"