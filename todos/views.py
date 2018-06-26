# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()[:10]
    context = {"todos":todos, "user": request.user}

    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id = id)
    context={"todo":todo, "user":request.user}

    return render(request, 'details.html', context)


def add(request):
    if(request.method == 'POST'):
        __title = request.POST['title']
        __text = request.POST['text']
        __filedata = request.FILES['file']
        
        addtodo = Todo(title=__title, text=__text, filedata=__filedata)
        addtodo.save()
        return redirect("/todos/")
    else:
        return render(request, 'add.html')    