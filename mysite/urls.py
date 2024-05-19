
from django.urls import path, include

urlpatterns = [
    path("books/", include("api.urls")),
    path("pizza/", include("pizzaAPI.urls")),
    path("employee/", include("employeeAPI.urls")),

    
]
