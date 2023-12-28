from django.shortcuts import render,redirect
from .forms import ExampleForm
from .import models

# Create your views here.


def DjangoForm(request):
    if request.method=="POST":
        fm=ExampleForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
    else:
        fm=ExampleForm()
                


    return render(request,"index.html",{"form": fm})


def model_form(request): 
    model_Form= models.Practice_model.objects.all()
    return render(request,"model.html",{'data':model_Form})

def delete_student(request,roll):
    std=models.Practice_model.objects.get(pk=roll).delete()
    return redirect("modelform")