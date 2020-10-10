from django.shortcuts import render, redirect
#!Import built-in django form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    #?I guess we have to add this whenever we are inheriting from UserCreationForm
    class Meta:
        #!We need this class to say that we want to save in user database
        model = User
        fields = ["username", "email", "password1", "password2"]