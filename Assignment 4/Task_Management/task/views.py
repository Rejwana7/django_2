from django.shortcuts import render,redirect
from . import forms
from .import models

# Create your views here.
def Add_Task(request):
    if request.method=="POST":
        fm = forms.TaskForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("homepage")
    else:
        fm = forms.TaskForm()


    return render (request,"add_task.html",{'form': fm })



def Edit_Task(request,id):
    editTask=models.TaskModel.objects.get(pk=id)
    fm = forms.TaskForm(instance=editTask)

    if request.method=="POST":
        fm = forms.TaskForm(request.POST,instance=editTask)
        if fm.is_valid():
            fm.save()
            return redirect("homepage")
    


    return render (request,"add_task.html",{'form': fm })

def Delete_Task(request,id):
     deleteTask=models.TaskModel.objects.get(pk=id)
     deleteTask.delete()
     return redirect("homepage")


