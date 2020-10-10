from django.shortcuts import render, redirect
#!Import built-in django form
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.

def register(response):
    #*Similar to creating a new todolist
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        #!Doesn't matter if password was valid or not. Just brings back to homepage
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
