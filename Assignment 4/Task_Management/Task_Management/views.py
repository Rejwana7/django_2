from django.shortcuts import render
from task.models import TaskModel

def home(request):
    task=TaskModel.objects.all()
    return render(request,"show_task.html" ,{'data': task})