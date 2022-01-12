from django.shortcuts import render ,HttpResponse

from app import models
from app.models import Task

# Create your views here.

def home(request):
    context= {'sucess':False}
    if request.method=='POST':
        title=request.POST['Title']
        des=request.POST['des']
        #date=request.POST['date']
        ins =Task(task_tittle=title,task_des=des)
        ins.save()
        context= {'sucess':True}

    return render(request,'index.html',context)

def task(request):
    alltasks=Task.objects.all()
    context={'tasks':alltasks}
    return render(request,'task.html',context)
