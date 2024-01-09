from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator #class decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here.
@login_required
def add_post(request):
    if request.method=="POST":

         post_form = forms.postForm(request.POST) #user post request data ekhane capture korlam
         if post_form.is_valid(): #post kora data gulo valid kina check kortesi
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save() #zodi data valid hoy database e save korbo
            # database save
            return redirect('add_post') #sob thik thakle add_catagory url e pathiye dibo

    else:
       post_form= forms.postForm() # user normally gele blank form pabe


    return render(request,"add_post.html" ,{'form': post_form})

# add post using class based view
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class= forms.postForm
    template_name='add_post.html'
    success_url= reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def Edit_post(request,id):
    post= models.Post.objects.get(pk=id)
    post_form= forms.postForm(instance=post)
    # print(post)
    if request.method=="POST":

         post_form = forms.postForm(request.POST,instance=post) #user post request data ekhane capture korlam
         if post_form.is_valid(): #post kora data gulo valid kina check kortesi
            post_form.instance.author=request.user
            post_form.save() #zodi data valid hoy database e save korbo
            # database save
            return redirect('homepage') #sob thik thakle add_catagory url e pathiye dibo

    # else:
    #    post_form= forms.postForm() # user normally gele blank form pabe


    return render(request,"add_post.html" ,{'form': post_form})  
    
# class based
@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model=models.Post
    form_class = forms.postForm
    template_name = "add_post.html"
    pk_url_kwarg = 'id'
    success_url= reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model=models.Post
    
    template_name = "delete.html"
    pk_url_kwarg = 'id'
   
 
    success_url= reverse_lazy('homepage')


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'    
    template_name = 'post_details.html'
    def post(self, request, *args,**kwargs):
        post = self.get_object() #sob object database theke niye astesi
        # Retrieves the specific Post object associated with this view. 
        if self.request.method =='POST':
                comment_form = forms.CommentForm(data=self.request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)
                    new_comment.post = post
                    # This line assigns the Post object (post) to the post field of the new_comment.
                    #This operation establishes a relationship between this newly created Comment and a specific Post. It links the comment to the post by setting the foreign key relationship between them. The post field in the Comment model refers to a Post object.
                    new_comment.save()
                return self.get(request, *args,**kwargs)  

    def get_context_data(self,**kwargs): #comment show
        context = super().get_context_data(**kwargs)
        post= self.object #post model er object ekhane store korlam
        #Retrieves the specific Post object associated with this view using self.object.
        comments=post.comments.all()
        comment_form = forms.CommentForm()
           
        context['comments']= comments
        context['comment_form'] = comment_form
        return context     
     
  
