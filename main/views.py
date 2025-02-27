from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {"title": "Главная страница сайта", "task": tasks})


def about(request):
    return render(request, 'main/about.html')


def createtask(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createtask.html', context)
