import os
from django.shortcuts import render,redirect
from .forms import Myfileform
from .models import Myfileupload
from django.contrib import messages

# Create your views here.
def home(request):
    mydata=Myfileupload.objects.all()
    myform= Myfileform()
    if mydata!=' ':
        context={'form':myform,'mydata':mydata}
        return render(request,"home.html",context)
    else:
        context={'form':myform}
        return render(request,"home.html",context)

def uploadfile(request):
    if request.method=="POST":
        myform=Myfileform(request.POST,request.FILES)
        if myform.is_valid():
            MyFileName=request.POST.get('file_name')
            MyFile=request.FILES.get('file')

            exists=Myfileupload.objects.filter(file=MyFile).exists()

            if exists:
                messages.error(request,'The file %s is already exists....!'% MyFile)

            else:
                Myfileupload.objects.create(file_name=MyFileName,file=MyFile).save()
                messages.success(request,"file uploaded successfully...")

        return redirect("home")

def deleteFile(request,id):
    mydata= Myfileupload.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.file.path)
    messages.success(request,"file successfully deleted...")
    return redirect('home')