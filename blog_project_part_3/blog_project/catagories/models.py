from django.db import models

# Create your models here.
class Catagory(models.Model):
    name= models.CharField(max_length=150)
    slug= models.SlugField(max_length=200, unique=True , null=True,blank=True)
    

    def __str__(self):
        return self.name