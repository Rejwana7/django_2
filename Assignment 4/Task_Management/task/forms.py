from django import forms

from .models import TaskModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields= '__all__'
        labels={
            "tasktitle": "Task Title",
            "taskdescription": "Task Description",
            "is_completed" : "Task Completed",
            "task_assign_date":"Task Assign Date",
            "categories":"Categories",

             
        }

        widgets={
             "task_assign_date" : forms.DateInput(attrs={'type': "date"}),
             "categories": forms.CheckboxSelectMultiple
             
              
        }