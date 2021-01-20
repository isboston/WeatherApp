from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["city", "temperature"]
        widgets = {
            "city": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the city'
            }),
            "temperature": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the temperature'
            }),
        }
