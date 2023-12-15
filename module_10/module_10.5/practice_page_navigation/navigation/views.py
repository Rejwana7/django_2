from django.shortcuts import render
import datetime

# Create your views here.

def navigate(request):
   # return render(request,'navigation/navigate.html')
   dict={'Details':[
      {
        'name':'Abir',
        'Age':25,

      },
      {
        'name':'Abid',
        'Age':20,

      },
      {
        'name':'Rahim',
        'Age':23,

      },
      
  ] , "list":["Rakib","karim","Tahsan"]}
   return render(request,'navigation/navigate.html',dict)

def context(request):

    d={
        'list':['python' ,'is','fun','Happy','Coding'],
        'Birthday': datetime.datetime.now(),
        'Status':None,
        'person':[
            {
                "name":'Adiba',
                "Age":20
            },
              {
                "name":'Wasi',
                "Age":22
            },
             {
                "name":'Salma',
                "Age":23
            }, ],
        'Text':'<p>You are <em>pretty</em> smart!</p>',
        'Text_1':'He is Talented, Creative',
        'value':5,
         'Text_2':'January - February',
    }
    return render(request,'navigation/context.html',d)
