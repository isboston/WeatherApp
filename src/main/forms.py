from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Please enter the city'}))
    temperature = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Please enter the temperature'}))

    class Meta:
        model = Task
        fields = ('city', 'temperature', 'location', 'rainfall')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
