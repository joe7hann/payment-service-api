from .models import PaymentUser
from .serializers import PaymentUserSerializer
from rest_framework import viewsets 
from expired_payment.models import ExpiredPayment
from rest_framework.permissions import  AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend



from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
class PaymentUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_date','expiration_date']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        payment = PaymentUser.objects.get(pk=response.data['id'])
        penalty = payment.payment_date - payment.expiration_date
        penalty_int = int(penalty.total_seconds())

        if payment.payment_date > payment.expiration_date:
            expired_payment_data = {
                'penalty_fee_amount': penalty_int * 0.00001,
                'pay_user_id': payment.id,
            }
            expired_payment = ExpiredPayment.objects.create(**expired_payment_data)

            expired_payment.save()

        return response

