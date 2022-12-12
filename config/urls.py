from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/', include('shop.urls', namespace='api')),
]