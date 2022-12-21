from rest_framework import routers
from .views import PaymentUserViewSet

payment_user_router = routers.DefaultRouter()

payment_user_router.register(r'', PaymentUserViewSet,'payment_user')
urlpatterns = payment_user_router.urls

