from django.shortcuts import render,redirect
from . import models

import time

def home(request):
 return render(request,"home.html") 

def about(request):
 return render(request,"about.html")

def contact(request):
 return render(request,"contact.html")

def service(request):
 return render(request,"service.html")

def register(request):
 if request.method=="GET":      
  return render(request,"register.html",{"output":""})
 else:
  #print(request.POST)     
  name=request.POST.get("name")
  email=request.POST.get("email")    
  password=request.POST.get("password")
  mobile=request.POST.get("mobile")
  address=request.POST.get("address")
  city=request.POST.get("city")
  gender=request.POST.get("gender")
  info=time.asctime()

  p=models.Register(name=name,username=email,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",info=info)
  
  p.save()

  return render(request,"register.html",{"output":"User Register Successfully...."})     

def login(request):
 if request.method=="GET":  
  return render(request,"login.html",{"output":""})
 else:
  #to get user details to make login
  email=request.POST.get("email")
  password=request.POST.get("password")

  userDetails=models.Register.objects.filter(username=email,password=password,status=1)

  if len(userDetails)>0:
   if userDetails[0].role=="admin":  
    return redirect("/myadmin/") 
   else:
    return redirect("/user/")   
  else:
   return render(request,"login.html",{"output":"Invalid user or verify your account...."})          






