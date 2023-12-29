from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Roll= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=200)
    father_name= models.CharField(max_length=100)
    address= models.TextField()

    def __str__(self):
        return f' Name: {self.name} - {self.Roll}'
    