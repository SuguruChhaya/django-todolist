from django.db import models
from django.contrib.auth.models import User
#!Make todolist for the specific person
# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        #*Can be retrieved by ToDoList.objects.get()
        return self.name 

    


class Item(models.Model):
    #!To dolist will automatically have set that stores all the items
    #*ForeignKey helps connect the database of ToDoList to Item. Basically an Item will belong in a ToDo list. 
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    #*completed item in to do list or not
    complete = models.BooleanField()

    def __str__(self):
        return self.text