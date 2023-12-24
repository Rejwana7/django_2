from django import forms
from django.core import validators
#widgets == field to html input

class contactForm(forms.Form):
    name= forms.CharField(label="Full Name :",initial="Name",help_text="Total length must be within 70 charecters", required=False, 
    widget= forms.Textarea(attrs={'id':'text_area',
    'class': 'class1 class2','placeholder':'Enter your name'}))
    email= forms.EmailField(label="useremail")
   
    # age = forms.IntegerField()
    # weight= forms.FloatField()
    # balance = forms.DecimalField()
    check=forms.BooleanField()
    #birthday =forms.DateField(widget= forms.DateInput(attrs={'type':'date'})) 
    birthday =forms.CharField(widget= forms.DateInput(attrs={'type':'date'})) 
    age = forms.CharField(widget= forms.NumberInput)
    appointment =forms.DateTimeField(widget= forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L',"Large")]
    size = forms.ChoiceField(choices=CHOICES,widget= forms.RadioSelect)
    MEAL=[('P', 'Pepperoni'),('M',"Mashroom"),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices= MEAL,widget= forms.CheckboxSelectMultiple)

    #file= forms.FileField()

# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email= forms.CharField(widget= forms.EmailInput)  

#     # def clean_name(self):
#     #     valname= self.cleaned_data['name']
#     #     if len(valname)< 10:
#     #          raise forms.ValidationError("Enter a name with at least 10 character")
#     #     else:
#     #         return valname
#     # def clean_email(self):
#     #     valemail= self.cleaned_data['Email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Enter valid Email ending with .com")
#     #     else:
#     #         return valemail    

#     def clean(self):
#         cleaned_data =  super().clean()
#         valname = self.cleaned_data['name']
#         valemail= self.cleaned_data['email']
#         # if len(valname)< 10:
#         #       raise forms.ValidationError("Enter a name with at least 10 character")
#         # # else:
#         #     return valname

#         if '.com' not in valemail:
#             raise forms.ValidationError("Enter valid Email ending with .com")
#         # else:
#         #     return valemail     

#         if len(valname)< 10:
#               raise forms.ValidationError("Enter a name with at least 10 character")
#         # else:
#         #     return valname
 
def len_Check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a value with at least 10 character ")
class StudentData(forms.Form):
    name = forms.CharField(widget= forms.TextInput,validators=[validators.MaxLengthValidator
    (10,message='Enter a name with max 10 character')])
    Text = forms.CharField(widget= forms.TextInput,validators=[len_Check]) #function
    email= forms.CharField(widget= forms.EmailInput,validators=[validators.EmailValidator
    (message="Enter a valid email")])  
    age= forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(34,message="age must be maximum 34"),validators.MinValueValidator(24,message="age must be at least 24")])
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='File extebnsion must be ended with .pdf,.png')])
    #regex,url,pattern 

class PasswordvalidationProject(forms.Form):
    name= forms.CharField(widget=forms.TextInput)
    password= forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data= super().clean()
        username= self.cleaned_data['name']
        valpass = self.cleaned_data['password']
        val_conpass= self.cleaned_data['confirm_password']
        if val_conpass != valpass:
            raise forms.ValidationError("Password doesn't match")

        if len(username)<10:
            raise forms.ValidationError("Name must be at least 10 characters")   





 






   