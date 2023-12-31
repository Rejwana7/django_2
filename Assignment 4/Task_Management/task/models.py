from django.db import models
from category.models import CategoryModel

# Create your models here.

class TaskModel(models.Model):
    tasktitle= models.CharField(max_length=200,verbose_name="Task Title")
    taskdescription= models.CharField(max_length=200,verbose_name="Task Description")
    is_completed=models.BooleanField(default=False,verbose_name="Task Completed")
    task_assign_date=models.DateTimeField(verbose_name="Task Assign Date")
    categories=models.ManyToManyField(CategoryModel,verbose_name="Categories")

    def __str__(self):
        return self.tasktitle

