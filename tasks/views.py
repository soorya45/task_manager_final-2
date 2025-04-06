from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def task_form_view(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task-form')
    return render(request, 'tasks/task_form.html', {'form': form, 'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task-form')

def task_json(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return JsonResponse({'id': task.id, 'title': task.title, 'description': task.description})
