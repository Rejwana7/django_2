from django import forms
from first_app.models import StudentModel


class Student(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields='__all__'
        # exclude=['father_name']
        labels={
            'name' : 'Student Name',
            'Roll' : 'Student Roll',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': ''}),
            
        }
        help_texts ={
            'name' : "write your full name",

        }
        error_messages={
            'name' : { 'required':'Your name is required' }
        }


    
   
    
