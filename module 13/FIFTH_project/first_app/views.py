from django.shortcuts import render
from .forms import contactForm
from .forms import StudentData
from .forms import  PasswordvalidationProject

# Create your views here.
def home(request):
      return render(request, 'home.html')

def about(request):
      if request.method == 'POST':
        print(request.POST)
        name= request.POST.get('username')
        email= request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'about.html',{'name':name,'email':email ,'select':select})
      else:
        return render(request, 'about.html')

def submit_form(request):
    #print(request.POST)
    ##if request.method == 'POST':
       # name= request.POST.get('username')
        #email= request.POST.get('email')
        #return render(request,'form.html',{'name':name,'email':email})
    #else:

         return render(request,'form.html')

def DjangoForm(request):
  if request.method =='POST':
    form = contactForm(request.POST,request.FILES)
    #form object
    if form.is_valid():
    #  file=form.cleaned_data['file']
    #  with open('./first_app/upload/' + file.name, 'wb+') as destination:
    #       for chunck in file.chunks():
    #           destination.write(chunck)

     print(form.cleaned_data)

  #form =contactForm(request.POST)
  #form =contactForm()
  #print(form) pura code
  #if form.is_valid():
    #print(form.cleaned_data)  #value
      #return render(request, 'django_form.html',{'form':form})
  else:
    form= contactForm()  
  return render(request, 'django_form.html',{'form':form})  


def Studentform(request):
  if request.method=='POST':
    form=StudentData(request.POST,request.FILES)
    if form.is_valid():
      print(form.cleaned_data)
  else:
    form=StudentData()

  return render(request,'django_form.html', {'form':form})  

def checkpassword(request):
  if request.method=='POST':
    form=PasswordvalidationProject(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
  else:
    form=PasswordvalidationProject()

  return render(request,'django_form.html', {'form':form})       
    