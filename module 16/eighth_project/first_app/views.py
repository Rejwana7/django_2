from django.shortcuts import render,redirect

from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


# Create your views here.


def home(request):
    return render(request, 'home.html')

def signUp(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully')
                # messages.warning(request,'warning')
                # messages.info(request,'info')
            
                form.save()
            # print(form.cleaned_data)
        else:
            form=RegisterForm()     

        return render(request,"signup.html",{'form':form})
    else:
        return redirect('profilepage')    
    

def user_login(request):
    # Checks if the user is not already authenticated
    if not request.user.is_authenticated:
        # Checks if the request method is POST (usually when a form is submitted)
        if request.method== 'POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user= authenticate(username=name,password=userpass)
                # check kortechi user database e ache kina
                if user is not None:
                    login(request,user)
                    return redirect('profilepage')  #profile page e redirect korbe
        else:
             # If the request method is not POST, initializes an empty AuthenticationForm
            form=AuthenticationForm()
        # Renders the login.html template with the form (valid or empty)    
        return render(request,'./login.html',{'form':form}) #zodi valid na hoy return
    else:
        # Redirects the user to the 'profilepage' if already authenticated
        return redirect('profilepage')    


def profile(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            form=ChangeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account updated  Successfully')
                # messages.warning(request,'warning')
                # messages.info(request,'info')
            
                form.save()
            # print(form.cleaned_data)
        else:
            form=ChangeUserData(instance=request.user)     

        return render(request,"profile.html",{'form':form})
    else:
        return redirect('signup')   
    # if request.user.is_authenticated:
    #   return render(request,'./profile.html',{'user':request.user})     
    # else:
    #     return redirect('loginpage')     


def user_logout(request):
    logout(request)
    return redirect('loginpage')


def pass_change(request):
    if  request.user.is_authenticated:

        if request.method=="POST":
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user) #password update korbe
                #update_session_auth_hash(request,form.cleaned_data['user])
                return redirect('profilepage')

        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
      return redirect('loginpage')       

   

def pass_change2(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profilepage')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form}) 
    else:
        return redirect('loginpage')    


#def change_user_data(request):
    # if  request.user.is_authenticated:
    #     if request.method=="POST":
    #         form=ChangeUserData(request.POST,instance=request.user)
    #         if form.is_valid():
    #             messages.success(request,'Account updated  Successfully')
    #             # messages.warning(request,'warning')
    #             # messages.info(request,'info')
            
    #             form.save()
    #         # print(form.cleaned_data)
    #     else:
    #         form=ChangeUserData()     

    #     return render(request,"profile.html",{'form':form})
    # else:
    #     return redirect('signup')    
                      

