from django.shortcuts import render

def HomePage(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'Aboutus.html')
