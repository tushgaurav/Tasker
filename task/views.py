from django.shortcuts import render

tasks_list = []


def index(request):
    return render(request, "task/index.html")


def view(request):
    context = {"tasks": tasks_list}
    return render(request, "task/tasks.html", context)


def add(request):
    return render(request, "task/add.html")
