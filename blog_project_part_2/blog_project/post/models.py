from django.db import models
from catagories.models import Catagory
from author.models import Author

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=150)
    content=models.TextField()
    catrgory=models.ManyToManyField(Catagory) 
    # ekta post multiple catagories er moddhe thakte pare abar 
    # ekta catagorir moddhe multiple post thakte pare
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    # ekjon author multiple post lekhte pare


    def __str__(self):
        return self.title
