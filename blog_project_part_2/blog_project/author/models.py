from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=200)
    bio= models.TextField()
    phone_no= models.CharField(max_length=12)

    def __str__(self):
        return f"Name: {self.Name}"
    
    
