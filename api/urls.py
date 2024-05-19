from django.urls import path
from . import views


urlpatterns = [
    path("create", views.CreateBook.as_view(), name="books-view-create"),
    path("", views.GetAllBooks.as_view(), name="books-view-get"),
    path("<int:pk>", views.GetBooksById.as_view(), name="books-view-get"),    
    path("update/<int:pk>", views.UpdateBook.as_view(), name="books-view-update"),
    path("delete/<int:pk>", views.DeleteBook.as_view(), name="books-view-Delete"),


   
    
]