from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def weather(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
        else:
            error = 'incorrect input'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/weather.html', context)
