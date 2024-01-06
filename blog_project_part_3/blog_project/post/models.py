from django.db import models
from catagories.models import Catagory
# from author.models import Author

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=150)
    content=models.TextField()
    category=models.ManyToManyField(Catagory,null=True,blank=True) 
    # ekta post multiple catagories er moddhe thakte pare abar 
    # ekta catagorir moddhe multiple post thakte pare
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    # ekjon author multiple post lekhte pare
    image= models.ImageField(upload_to='post/media/uploads/',blank=True,null=True)


    def __str__(self):
        return self.title


class comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    body=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    # zokhon i e class er object make hobe sei time ta rekhe dibe
    def __str__(self):
        return f"Comments by {self.name}"