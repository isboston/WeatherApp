from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib import messages
from src.settings import EMAIL_HOST_USER
from .models import Task
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.filter(city__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


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
