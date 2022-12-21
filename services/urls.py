from rest_framework import routers
from .views import ServiceViewSet

service_router = routers.DefaultRouter()

service_router.register(r'', ServiceViewSet,'service')
urlpatterns = service_router.urls

