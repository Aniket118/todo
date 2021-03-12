from .forms import TaskForm
from django.shortcuts import redirect, render
from .models import Task, TaskList
from .forms import TaskForm,Task_List_Form
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login') 
def index(request):
    tasks = Task.objects.all()
    task_lists = TaskList.objects.all()
    return render(request, "trello_app/index.html", {'tasks':tasks, 'task_lists':task_lists})

@login_required(login_url='login') 
def add_task_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at)
        task_list.save()
        return redirect('index')
    return render(request, "trello_app/add_task_list.html")

@login_required(login_url='login') 
def add_task(request):
    if request.method == 'POST':
           form = TaskForm(data=request.POST)
           if form.is_valid():
               form.save()
               return redirect('index')

    else:
        form = TaskForm()

    return render(request, "trello_app/add_task.html", {'form':form})

@login_required(login_url='login') 
def add_task_list1(request):
    if request.method == 'POST':
           form = Task_List_Form(data=request.POST)
           if form.is_valid():
               form.save()
               return redirect('index')

    else:
        form = Task_List_Form()
    return render(request, "trello_app/add_task_list1.html", {'form':form})

