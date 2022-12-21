from .models import PaymentUser
from rest_framework import serializers


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = "__all__"
    


    
    
