from django.urls import path
from . import views

urlpatterns=[
    #path('',views.TodoListView),
    path('api/todos/', views.todos_list, name='todo-list'),
    path('', views.TodoListView.as_view(), name='todo-list'),
]