from django.db import models
from django.contrib.auth.models import User

#Defining models
class Company(models.Model):
    name = models.CharField(max_length=100)
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)

class Transaction(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    # ForeignKey relationship with the device model indicating the device associated with this transaction.
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # ForeignKey relationship with the employee model indicating the employee associated with this transaction.
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField()
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=100)
