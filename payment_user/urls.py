from rest_framework import routers
from .views import PaymentUserViewSet, RemittanceViewSet, OverdueViewSet,RemittanceAdminViewSet, OverdueAdminViewSet
from django.urls import path
payment_user_router = routers.DefaultRouter()

payment_user_router.register('', PaymentUserViewSet,'payment_user')
urlpatterns = [
    path('remittance/<user_id>/', RemittanceViewSet.as_view(), name="remittance"),
    path('overdue/<user_id>/', OverdueViewSet.as_view(), name="overdue"),
    path('remittance/', RemittanceAdminViewSet.as_view(), name="remittance-admin"),
    path('overdue/', OverdueAdminViewSet.as_view(), name="overdue-admin"),

]
urlpatterns += payment_user_router.urls





