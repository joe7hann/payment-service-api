from django.db import models
from payment_user.models import PaymentUser
# Create your models here.

class ExpiredPayment(models.Model):
    #pay_user_id
    pay_user = models.OneToOneField(PaymentUser,on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.penalty_fee_amount)
    class Meta:
        db_table = 'expired_payment'