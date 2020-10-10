"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#!Import form url cuz we are in different directory
from register import views as v

#*Direct to specific pages

urlpatterns = [
    #!When additional url is typed after server name, it is searched in man.urls
    path('admin/', admin.site.urls),
    #*If nothing is typed, site will be directed to main.urls
    path("", include("main.urls")),
    #*Create new redirection to the login form
    #!Opposed to include where we have to check what link is trailing after, we can directly lead to a website
    path("register/", v.register, name="register"),
    #*Have to login stuff
    #*Automatically looks for these urls for us
    #!Create a registration folder in one of the templates folder (I created it in )
    path('', include("django.contrib.auth.urls"))
]
