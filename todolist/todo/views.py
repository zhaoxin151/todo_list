from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from .models import Todo

def todoList(request):
    todolist = Todo.objects.all()
    return render(request, 'todo/todolist.html', {'todolist': todolist})

def completetodo(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    if todo_item.flag == '1':
        todo_item.flag = '0'
        todo_item.save()
        return HttpResponseRedirect('/todo/')
    todolist = Todo.objects.all()
    return render(request, 'todo/todolist.html', {"todolist": todolist})

def resettodo(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    if todo_item.flag == '0':
        todo_item.flag = '1'
        todo_item.save()
        return HttpResponseRedirect('/todo/')
    todoList = Todo.objects.all()
    return render(request, 'todo/todolist.html', {"todolist": todoList})

def deletetodo(request, todo_id):
    try:
        todo_item = Todo.objects.get(id=todo_id)
    except Exception:
        raise Http404
    if todo_item:
        todo_item.delete()
        return HttpResponseRedirect('/todo/')
    todoList = Todo.objects.all()
    return render(request, 'todo/todolist.html', {"todolist": todoList})

def edittodo(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    return render(request, 'todo/edit_todo.html', {"todo_item": todo_item})

def savetodo(request, todo_id):
    # return HttpResponseRedirect('/todo/')
    try:
        todo_item = Todo.objects.get(id=todo_id)
    except Exception:
        raise Http404
    if todo_item:
        todo_item.todo = request.POST['todo']
        todo_item.flag = request.POST['flag']
        todo_item.priority = request.POST['priority']
        todo_item.save()
        return HttpResponseRedirect('/todo/')
    todoList = Todo.objects.all()
    return render(request, 'todo/todolist.html', {"todolist": todoList})

def addtodo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        priority = request.POST['priority']
        todo_item = Todo(todo=todo, priority=priority, flag='1')
        todo_item.save()
        todoList = Todo.objects.all()
        return render(request, 'todo/todolist.html', {"todolist": todoList})
    else:
        return render(request, 'todo/add_todo.html')
