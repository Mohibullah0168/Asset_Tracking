


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Employee, Device, Transaction
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Checking if the user is associated with an employee
        if not hasattr(self.request.user, 'employee'):
            return Transaction.objects.none() # If not associated, return empty queryset

        # Get the current user's company and employee
        user_company = self.request.user.employee.company
        user_employee = self.request.user.employee

        # Filter transactions based on the user's association with the company
        queryset = Transaction.objects.filter(company=user_company, employee=user_employee)
        return queryset

    def create(self, request, *args, **kwargs):
        # Check if the user is associated with an employee
        if not hasattr(request.user, 'employee'):
            return Response({'detail': 'User is not associated with an employee'}, status=status.HTTP_403_FORBIDDEN)
        
        # Continue with the default create method
        return super().create(request, *args, **kwargs)
