from django.db import models
#from django.contrib.auth.models import User
from users.models import User
from datetime import datetime
from services.models import Service

# Create your models here.
class PaymentUser(models.Model):
    #user_id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #service_id
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    payment_date = models.DateTimeField(default=datetime.now)
    expiration_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Service: '+str(self.service)+ ' User: ' +str(self.user)
    # def __str__(self):
    #     return self.id

    class Meta:
        db_table = 'payment_user'