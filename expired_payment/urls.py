from rest_framework.routers import DefaultRouter
from .views import ExpiredPaymentViewSet

expired_payment_router = DefaultRouter()

expired_payment_router.register(r'',ExpiredPaymentViewSet, 'expired_payment')

urlpatterns = expired_payment_router.urls