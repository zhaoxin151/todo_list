from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todoList, name='todolist'),
    path('completetodo/<int:todo_id>', views.completetodo, name="completetodo"),
    path('resettodo/<int:todo_id>', views.resettodo, name="resettodo"),
    path('deletetodo/<int:todo_id>', views.deletetodo, name='deletetodo'),
    path('edittodo/<int:todo_id>', views.edittodo,name='edittodo'),
    path('savetodo/<int:todo_id>', views.savetodo, name='savetodo'),
    path('addtodo/', views.addtodo, name='addtodo'),
]