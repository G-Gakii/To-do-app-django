from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todoItems
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Homepage(request):
    if request.method =='POST':
        task=request.POST.get('task')
        new_task=todoItems(user=request.user,item_name=task)
        new_task.save()
    all_todos=todoItems.objects.filter(user=request.user)
    context={
        'todos':all_todos
    }
    return render(request,'todoapp/todo.html',context)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method =='POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password=request.POST.get("password")
        if len(password) < 4:
            messages.error(request,'password must be atleast 4 characters')
            return redirect('register')
        
        get_users_by_username=User.objects.filter(username=username)
        if get_users_by_username:
            messages.error(request,"username already exist")
            return redirect('register')
        
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        return redirect('logIn')

        
    
    return render(request,'todoapp/register.html',{})
def logOut(request):
    logout(request)
    return redirect('logIn')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method =="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")

        validate_user=authenticate(username=username, password=password)
        if validate_user is not None:
            login(request , validate_user)
            messages.success(request,"account successfully created,log in now")
            return redirect('homepage')
        else:
            messages.error(request,'wrong user details or user does not exist')
          
            return redirect('logIn')


    return render(request,'todoapp/login.html',{})
@login_required
def deleteTask(request,name):
    get_todo= todoItems.objects.get(user=request.user,item_name=name)
    get_todo.delete()
    return redirect('homepage')

@login_required
def updateTask(request,name):
    get_todo= todoItems.objects.get(user=request.user,item_name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('homepage')

