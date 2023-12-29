from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=20)
    Roll= models.IntegerField(primary_key=True)
    address= models.TextField()
    fathers_name= models.TextField(default="Rahim")

    def __str__(self):
        # return self.name
        return f"Roll : {self.Roll} - {self.name}"
    