from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer


class CreateBook(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class GetAllBooks(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer   

class GetBooksById(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer     
    lookup_field = "pk" 

class UpdateBook(generics.RetrieveUpdateDestroyAPIView):
     queryset = Books.objects.all()
     serializer_class = BooksSerializer     
     lookup_field = "pk" 

class DeleteBook(generics.DestroyAPIView):
     queryset = Books.objects.all()
     serializer_class = BooksSerializer     
     lookup_field = "pk"      