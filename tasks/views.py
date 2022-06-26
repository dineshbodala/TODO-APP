from asyncio import tasks
from multiprocessing import context
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path, reverse_lazy
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task


def loginpage(request):
    
    if 1>0:
        form=UserCreationForm()
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/', user)
            else:
                messages.info(request, 'Invalid Credentials')
           
        context={'form':form}
        return render(request,'tasks/login.html', context)

def logoutuser(request):
    return redirect('login')

@login_required(login_url='login')
def index(request):
    tasks= Task.objects.filter(owner=request.user)
    form= TaskForm()
    context={'tasks':tasks, 'form':form}
    if request.method=='POST':
        form=TaskForm(request.POST)
        form.save()
        return redirect('/')
    
    return render(request, 'tasks/list.html', context)









@login_required(login_url='login')
def updatetask(request,pk):
    tasks= Task.objects.get(id=pk)
    form= TaskForm(instance=tasks)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deletetask(request, pk):
    task=Task.objects.get(id=pk)
    context={'task':task}
    if request.method=='POST':
        task.delete()
        return redirect("/")
    return render(request, 'tasks/delete.html', context)




   
    
    



# Create your views here.
