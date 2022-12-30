from rest_framework import routers
from .views import PaymentUserViewSet, RemittanceViewSet, OverdueViewSet
from django.urls import path
payment_user_router = routers.DefaultRouter()

payment_user_router.register('', PaymentUserViewSet,'payment_user')
urlpatterns = [
    path('remittance/<user_id>/', RemittanceViewSet.as_view(), name="remittance"),
    path('overdue/<user_id>/', OverdueViewSet.as_view(), name="overdue"),

]
urlpatterns += payment_user_router.urls





