from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    dic = {'author':'Rahim','age':25,'list':['python','is', 'good'], 'birthday':datetime.datetime.now(),
    'val':None ,'Name': 'karim is','courses':[
        {
            'id':1,
            'name':'python',
            'fee':5000,
        },
        {
            'id':2,
            'name':'Algorihm',
            'fee':6000
        
        },
        {
            'id':3,
            'name':'C',
            'fee':2000
        
        },
    ]}

    return render (request,'home.html',dic)