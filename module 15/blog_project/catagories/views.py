from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_catagory(request):
    if request.method=="POST":

         catagory_form = forms.catagoryForm(request.POST) #user post request data ekhane capture korlam
         if catagory_form.is_valid(): #post kora data gulo valid kina check kortesi
            catagory_form.save() #zodi data valid hoy database e save korbo
            # database save
            return redirect('add_catagory') #sob thik thakle add_catagory url e pathiye dibo

    else:
       catagory_form= forms.catagoryForm() # user normally gele blank form pabe


    return render(request,"add_category.html" ,{'form': catagory_form})
    

