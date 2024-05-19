
from django.urls import path, include

urlpatterns = [
    path("books/", include("bookAPI.urls")),
    path("pizza/", include("pizzaAPI.urls")),
    path("employee/", include("employeeAPI.urls")),

    
]
