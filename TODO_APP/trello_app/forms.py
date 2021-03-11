from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Task,TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
        }

class Task_List_Form(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = '__all__'
        widgets = {
            'created_at': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class':'datetimefield'}),
        }