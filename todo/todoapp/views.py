from django.shortcuts import render, redirect
from .models import TodoModel

# Create your views here.
def home(request):
    tasks = TodoModel.objects.all()
    context = {
       'tasks': tasks, 
    }
    return render(request, "todoapp/index.html", context=context)

def add(request):
    task = request.POST['task']
    TodoModel(task=task).save()
    return redirect('home')

def delete(request, pk):
    task = TodoModel.objects.filter(id=pk)
    task.delete()
    return redirect('home')

def update(request, pk):
    task = TodoModel.objects.filter(id=pk)[0]
    context = {
        'task': task,
    }
    return render(request, "todoapp/update.html", context=context)

def edit(request, pk):
    task = request.POST['task']
    todo = TodoModel.objects.filter(id=pk)[0]
    todo.task = task
    todo.save()
    return redirect('home')
