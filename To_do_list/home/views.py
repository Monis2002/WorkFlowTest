from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def all_clear(request):
    Task.objects.all().delete()
    return redirect('task_list')

def task_edit(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=task)
    return render(request,'task_edit.html',{'form':form,'task':task})
