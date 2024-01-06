from django import forms

from . models import Post,comment


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields= '__all__'
        exclude=['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields= ['name','email','body']
        
