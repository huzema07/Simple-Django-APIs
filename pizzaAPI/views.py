from django.shortcuts import render
from rest_framework import generics
from .models import Pizza
from .serializers import PizzaSerializer

# Create your views here.


class CreatePizza(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class GetAllPizzas(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer  

class GetPizzaById(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer     
    lookup_field = "pk"     

class UpdatePizza(generics.RetrieveUpdateDestroyAPIView):
     queryset = Pizza.objects.all()
     serializer_class = PizzaSerializer     
     lookup_field = "pk"     

class DeletePizza(generics.DestroyAPIView):
     queryset = Pizza.objects.all()
     serializer_class = PizzaSerializer     
     lookup_field = "pk"      