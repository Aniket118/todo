from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('add_task_list',views.add_task_list, name='add_task_list'),
    path('add_task_list1',views.add_task_list1, name='add_task_list1'),
    path('add_task',views.add_task,name='add_task'),
]