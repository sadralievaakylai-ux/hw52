from django.shortcuts import render, redirect
from webapp.models import Task, STATUS_CHOICES
from django.shortcuts import get_object_or_404
from django.urls import reverse


def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        if description and status in dict(STATUS_CHOICES):
            Task.objects.create(description=description, status=status, due_date=due_date or None)
        return redirect(reverse('task_list'))


def task_delete_view(request, task_id):
    if request.method == 'POST':
        Task.objects.filter(id=task_id).delete()
    return redirect(reverse('task_list'))

def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})
