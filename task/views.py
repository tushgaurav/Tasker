from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "task/index.html")


def tasks(request):
    return render(request, "task/tasks.html")
