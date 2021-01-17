from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["city", "temperature"]
        widgets = {
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the city'
            }),
            "temperature": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the temperature'
            }),
        }
