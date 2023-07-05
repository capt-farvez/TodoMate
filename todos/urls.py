from django.urls import path
from . import views

urlpatterns=[
    #path('',views.TodoListView),
    path('api/todos/', views.todos_list, name='todo-list'),
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('add/', views.addTodo, name='add-todo'),
    path('todo/<int:pk>/delete/', views.delete_todo, name='delete-todo'),
    path('todo/<int:pk>/update/', views.update_todo, name='update-todo'),
]