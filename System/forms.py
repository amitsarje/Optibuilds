from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import *


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields= [
             'username' , 'password' ,'first_name','last_name' , 'email'
        ]