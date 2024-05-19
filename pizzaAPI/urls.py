from django.urls import path, include
from . import views

# Your URL patterns for the pizzaAPI app go here

urlpatterns = [
        path("create", views.CreatePizza.as_view(), name="pizza-view-create"),
        path("", views.GetAllPizzas.as_view(), name="pizzas-view-get"),
        path("<int:pk>", views.GetPizzaById.as_view(), name="pizza-view-get"),
        path("update/<int:pk>", views.UpdatePizza.as_view(), name="pizza-view-update"),
        path("delete/<int:pk>", views.DeletePizza.as_view(), name="pizza-view-Delete"),

    


]
