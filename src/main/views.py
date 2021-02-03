from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib import messages
from src.settings import EMAIL_HOST_USER
from .models import Task, Rainfall
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskListSerializer
from django.db.models import Q


class Search(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Task.objects.filter(
            Q(city__icontains=query) | Q(temperature__icontains=query)
        )
        return object_list


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


class About(TemplateView):
    template_name = "main/about.html"


def weather(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'incorrect input'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'snow': Rainfall(type='Snow'),
        'rain': Rainfall(type='Rain'),
        'hailstorm': Rainfall(type='Hailstorm'),
        'frost': Rainfall(type='Frost'),
        'fog': Rainfall(type='Fog'),
    }
    return render(request, 'main/weather.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            mail = send_mail(
                'Weather registered',
                'You have successfully registered on the WEATHERAPP',
                EMAIL_HOST_USER,
                ['itvibn@mail.ru'],  # change mail
                fail_silently=False,
            )

            if mail:
                messages.success(request, 'You have successfully registered')
            else:
                messages.error(request, 'Sending error')
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


def search(request):
    return render(request, 'main/search.html')


class TaskView(APIView):
    def get(self, request):
        task = Task.objects.all()
        serializer = TaskListSerializer(task, many=True)
        return Response(serializer.data)
