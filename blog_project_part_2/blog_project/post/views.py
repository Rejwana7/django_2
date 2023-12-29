from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def add_post(request):
    if request.method=="POST":

         post_form = forms.postForm(request.POST) #user post request data ekhane capture korlam
         if post_form.is_valid(): #post kora data gulo valid kina check kortesi
            post_form.save() #zodi data valid hoy database e save korbo
            # database save
            return redirect('add_post') #sob thik thakle add_catagory url e pathiye dibo

    else:
       post_form= forms.postForm() # user normally gele blank form pabe


    return render(request,"add_post.html" ,{'form': post_form})



def Edit_post(request,id):
    post= models.Post.objects.get(pk=id)
    post_form= forms.postForm(instance=post)
    # print(post)
    if request.method=="POST":

         post_form = forms.postForm(request.POST,instance=post) #user post request data ekhane capture korlam
         if post_form.is_valid(): #post kora data gulo valid kina check kortesi
            post_form.save() #zodi data valid hoy database e save korbo
            # database save
            return redirect('homepage') #sob thik thakle add_catagory url e pathiye dibo

    # else:
    #    post_form= forms.postForm() # user normally gele blank form pabe


    return render(request,"add_post.html" ,{'form': post_form})  
    


def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
