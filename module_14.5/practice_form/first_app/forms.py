from django import forms
from django.core import validators
import datetime


class ExampleForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(),  label="Full Name:", validators=[
        validators.MinLengthValidator(12,message="Enter a name with  at least 12 Character")
    ])
    email=forms.EmailField()
    age=forms.IntegerField(widget=forms.NumberInput, required=False)
    roll=forms.IntegerField(help_text="Enter 6 digit")
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    day=forms.DateField(initial=datetime.date.today)
    appointment= forms.DateField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    value=forms.DecimalField()

    Favourite_Colors_Choices=[
        ('blue','Blue'),
        ('green','Green'),
        ('black','Black'),
    ]
    favourite_color=forms.ChoiceField(widget=forms.RadioSelect, choices=Favourite_Colors_Choices)
    favourite_colors=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Favourite_Colors_Choices)
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree=forms.BooleanField()