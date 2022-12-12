from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('api', views.EntityViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]