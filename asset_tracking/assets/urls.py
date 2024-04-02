from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, TransactionViewSet
# Defining urls for api endpoints
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
# Registering other viewsets

urlpatterns = [
    path('', include(router.urls)),
]