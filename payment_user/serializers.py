from .models import PaymentUser
from expired_payment.models import ExpiredPayment
from rest_framework import serializers


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = "__all__"
    
class RemittanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = ['id', 'user', 'service', 'amount', 'payment_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['service_name'] = instance.service.name
        data['service_logo'] = instance.service.logo
        return data

class OverdueSerializer(serializers.ModelSerializer):
    penalty_fee_amount = serializers.CharField(source='expiredpayment.penalty_fee_amount')

    class Meta:
        model = PaymentUser
        fields = ['user', 'service', 'amount', 'payment_date', 'expiration_date', 'penalty_fee_amount']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['service_name'] = instance.service.name
        data['service_logo'] = instance.service.logo
        return data


    

    
    
