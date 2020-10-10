from django.shortcuts import render
#*Import some stuff
from django.http import HttpResponse

#!I will get the to-do list based on the id
from .models import ToDoList, Item
from .forms import CreateNewList
from django.http import HttpResponseRedirect
# Create your views here.

def index(response, id):
    #*Receive
    #!This statement raises an error by receiving id of non existing to do list
    #!By commenting it, I can put in any integer and it will work
    #ls = ToDoList.objects.get(id=id)
    #*This item_set.all() returns a set so I cannot do item.text
    #*I have to specify the id
    #*Actually using the html templates
    ls = ToDoList.objects.get(id=id)
    #*Passing to-do list name as variable

    #!Check whether todolist belongs to the user. If not, he shouldn't be able to see it.
    if ls in response.user.todolist.all():
        #*Check whether posting or getting things
        #!Like create, inital view will just be getting things, but we are posting when we are making modifications
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    item.save()
                
            elif response.POST.get("newItem"):
            
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        else:
            pass
        return render(response, "main/list.html", {"ls": ls})

    #*Not own todolist
    else:
        return HttpResponseRedirect("/view")

def home(response):
    #!Have to pass something in because home is extention of base
    #!Have to name html folder templates
    return render(response, "main/home.html", {})

def create(response):
    #!Response is not just a garbage variable
    #*Response can tell whether we are trying to post or get something

    #*Give me the user
    #response.user check who is logging in
    if response.method == "POST":
        #?When clicking the the create method
        #*response.POST saves all the values, ids etc
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            #?When all required fields are filled
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            #?What is the difference between todolist_set.create and todolist.add
            response.user.todolist.add(t)
            #!Ultimately create new todolist
            

        #*Redirects to the todolist link
        return HttpResponseRedirect("/%i" %t.id)
    else:
        #?When initially loading up the new form page with no info, this is ran
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

#!2 main ways the server can receive information from form: post and get
#*Post when send to database etc (more encrypted)

def view(response):
    return render(response, "main/view.html", {})