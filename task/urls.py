from django.urls import path

from task import views

urlpatterns = [
    # create task url
    path('create/', views.CreateTask.as_view(), name='create_task'),
    # view task url
    path('view/<int:pk>/', views.ViewTask.as_view(), name='view_task'),
    # task list url
    path('list/', views.TaskList.as_view(), name='task_list'),
    # update task url
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update_task'),
    # delete task url
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),
]
