from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    projects = Projects.objects.all()
    return render(request,'index.html',{"projects":projects})

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


def rate(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    project = Projects.objects.get(id = id)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RateForm()
    return render(request,"rate.html",{"form":form,"project":project})