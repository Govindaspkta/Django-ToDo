from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create( task=task,)
    return redirect('homepage')

def mark_as_done(request,pk):
    task= get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    
    return redirect('homepage')
        
def mark_as_undone(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    
    return redirect('homepage')
