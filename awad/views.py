from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
def index(request):
    projects = Projects.objects.all()
    return render(request,'index.html',{"projects":projects})

@login_required(login_url='login')
def addProject(request):
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context= {'form':form}
    return render(request, 'newProject.html',context)


def projects(request,id):
    proj = Projects.objects.get(id = id)
    return render(request,'readmore.html',{"projects":proj})

@login_required(login_url='login')
def rate(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    user = request.user
    project = Projects.objects.get(id = id)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RateForm()
    return render(request,"rate.html",{"form":form,"project":project})

def registerPage(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
      
            messages.success(request, 'account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
                messages.info(request,'Username or password is incrorrect')
    context = {}
    return render(request, 'login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('index')
@login_required(login_url='login')
def profile(request, id):
    user = request.user.id
    pof = Profile.objects.get_or_create(user_id=id)
    print(pof)
    context = {'pof':pof}
    return render(request, 'profile.html', context)