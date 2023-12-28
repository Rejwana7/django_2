from django.db import models

# Create your models here.

class Practice_model(models.Model):
    name=models.CharField(max_length=250)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    s_class = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name} - {self.roll}"