from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, TaskForm
from .models import Task


@login_required
def complete_task(request, pk):
    if request.method == 'POST':
        Task.objects.filter(pk=pk, user=request.user).update(is_completed=True)
        return redirect('tasks')
    else:
        return HttpResponse('method is not allowed')


@login_required
def delete_task(request, pk):
    if request.method == 'POST':
        Task.objects.get(pk=pk, user=request.user).delete()
        return redirect('tasks')
    else:
        return HttpResponse('method is not allowed')


@login_required
def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)
    return render(request, 'core/tasks.html', {'user': request.user, 'tasks': user_tasks})


@login_required
def add_task(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'core/add_task.html', {'form': form})

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'core/add_task.html', {'form': form})


@login_required
def task_detail(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'core/task_detail.html', {'task': task})
    elif request.method == 'POST':
        Task.objects.get(pk=pk, user=request.user).delete()
        return redirect('tasks')


@login_required
def task_edit(request, pk):  # set the request method here update
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'core/task_edit.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            return render(request, 'core/task_edit.html', {'form': form})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

