from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    return render(request,'accounts/HomePage.html')

@login_required(login_url='login')
def about(request):
    gd = Grades.objects.all()

    return render(request,'accounts/about.html',{'gd':gd})


def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created succefully')
            return redirect('login')
    context = {'form':form}

    return render(request,'accounts/register.html',context)



def loginpage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Username or password is incorrect')
            return redirect('login')

    return render(request,'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def feedback(request):
    return render(request,'accounts/feedback.html')

@login_required(login_url='login')
def myprojects(request):
    mp = Projects.objects.all()

    return render(request,'accounts/myprojects.html',{'mp':mp})

@login_required(login_url='login')
def extracurricular(request):
    ec = ExtraCurricular.objects.all()

    return render(request,'accounts/extracurricular.html',{'ec':ec})
