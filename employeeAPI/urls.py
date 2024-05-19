from django.urls import path, include
from . import views

# Your URL patterns for the EmployeesAPI app go here

urlpatterns = [
        path("create", views.CreateEmployee.as_view(), name="Employee-view-create"),
        path("", views.GetAllEmployees.as_view(), name="Employees-view-get"),
        path("<int:pk>", views.GetEmployeeById.as_view(), name="Employee-view-get"),
        path("update/<int:pk>", views.UpdateEmployee.as_view(), name="Employee-view-update"),
        path("delete/<int:pk>", views.DeleteEmployee.as_view(), name="Employee-view-Delete"),

#this is a dummy comment

    


]
