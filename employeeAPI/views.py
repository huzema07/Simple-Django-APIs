from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


class CreateEmployee(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class GetAllEmployees(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer  

class GetEmployeeById(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer     
    lookup_field = "pk"     

class UpdateEmployee(generics.RetrieveUpdateDestroyAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer     
     lookup_field = "pk"     

class DeleteEmployee(generics.DestroyAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer     
     lookup_field = "pk"      