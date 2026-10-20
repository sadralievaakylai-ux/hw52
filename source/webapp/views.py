from django.shortcuts import render, redirect
from webapp.models import Task, STATUS_CHOICES


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
        return redirect('/')


def task_delete_view(request, task_id):
    if request.method == 'POST':
        Task.objects.filter(id=task_id).delete()
    return redirect('/')
