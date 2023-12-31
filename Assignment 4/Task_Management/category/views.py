from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def Add_Category(request):
    if request.method=="POST":
        fm = forms.CategoryForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("add_category")
    else:
        fm = forms.CategoryForm()


    return render (request,"add_catagories.html",{'form': fm })


def Edit_Category(request,id):
    editTask=models.CategoryModel.objects.get(pk=id)
    fm = forms.CategoryForm(instance=editTask)

    if request.method=="POST":
        fm = forms.CategoryForm(request.POST,instance=editTask)
        if fm.is_valid():
            fm.save()
            return redirect("homepage")
    


    return render (request,"add_catagories.html",{'form': fm })
