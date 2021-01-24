from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Task




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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')