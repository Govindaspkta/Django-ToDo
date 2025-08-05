from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
def addtask(request):
    task=request.POST['task']
    Task.objects.create( task=task,)
    return redirect('homepage')

def mark_as_done(request,pk):
    return HttpResponse(pk)