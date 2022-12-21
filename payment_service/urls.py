from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

# Nuevos imports añadidos
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Vista general e información de la API
schema_view = get_schema_view(
   openapi.Info(
      title="Service Payment API",
      default_version='v2',
      description="Service Payment API, proyecto desarrollo en silabuz",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="joe@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/users/', include('users.urls')),
    path('api/v2/services/', include('services.urls')),
    path('api/v2/payment-user/', include('payment_user.urls')),
    path('api/v2/expired-payment/', include('expired_payment.urls')),
    # Nuevas rutas añadidas
    path('api-docs/', include('rest_framework_swagger.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
