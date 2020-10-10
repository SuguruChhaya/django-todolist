from django.urls import path 

from . import views 


#*If user is on mainpage, views.index will be shown
urlpatterns = [
    #*id is whatever number that gets inputted in the url. Will be passed as argument
    #!The first int: part converts into integer. string does the similar thing
    #!The second :id part is the parameter name
    path("<int:id>", views.index, name="index"), 
    #*Creating a homepage which doesn't have any additional url
    #*Name= has not purpose
    path("", views.home, name="home"),
    #!New path for creating
    #*Always include backslash cuz that includes backslash and no backslash
    path("create/", views.create, name="home"),
    path("view/", views.view, name="view")
    
]