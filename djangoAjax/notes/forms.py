
# from django import forms
# def UserSignUp(forms.Form):
#     name = forms.CharField(max_length=100,required=True)
#     user_name= forms.CharField(max_length=100,required=True)
#     email=forms.EmailField(max_length=15,required=True)
#     password= forms.CharField(max_length=100,required=True)
#     repassword= forms.CharField(max_length=100,required=True)
from cProfile import label
from dataclasses import fields
import email
from pyexpat import model
from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from .models import Note

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,required=True,label="name")
    user_name = forms.CharField(max_length=50,required=True,label="user name")
    email = forms.EmailField(max_length=100,required=True,label="email")
    password = forms.CharField(max_length=50,widget=forms.PasswordInput,required=True,label="password")
    repassword = forms.CharField(max_length=50,required=True,label="re enter password")

# Login Form

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields="username","password"


class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=["title","description"]