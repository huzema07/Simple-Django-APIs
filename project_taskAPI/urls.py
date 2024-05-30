from django.urls import path, include
from . import views


urlpatterns = [

# Views for Project
    
        path("project/create", views.CreateProject.as_view(), name="project-view-create"),
        path("project", views.GetAllProjects.as_view(), name="projects-view-get"),
        path("project/<int:pk>", views.GetProjectById.as_view(), name="project-view-get"),
        path("project/update/<int:pk>", views.UpdateProject.as_view(), name="project-view-update"),
        path("project/delete/<int:pk>", views.DeleteProject.as_view(), name="project-view-Delete"),
       
        

        

#***************************************************************************
# Views for Task

        path("task/create", views.CreateTask.as_view(), name="task-view-create"),
        path("task", views.GetAllTasks.as_view(), name="tasks-view-get"),
        path("task/<int:pk>", views.GetTaskById.as_view(), name="task-view-get"),
        path("task/update/<int:pk>", views.UpdateTask.as_view(), name="task -view-update"),
        path("task/delete/<int:pk>", views.DeleteTask.as_view(), name="task-view-Delete"),
       




]
