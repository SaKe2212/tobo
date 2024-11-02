from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm



def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')

    else:
        form = TaskForm()
    return render(request, 'task_1/task_form.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_1/task_list.html', {'tasks': tasks})


def task_edit(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task_1/task_form.html', {"form": form})


def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')




