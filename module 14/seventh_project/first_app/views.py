from django.shortcuts import render
from first_app.forms import Student


# Create your views here.
def home(request):
    # std= Student()
    if request.method=="POST":
        form= Student(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            form.save()
            print(form.cleaned_data)
    else:
        form= Student()        
    return render(request,'home.html',{'form':form})