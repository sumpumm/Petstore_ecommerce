from django.shortcuts import render

def HomePage(request):
    return render(request,'petstore.html')

def AboutUs(request):
    return render(request,'Aboutus.html')

def Products(request):
    return render(request,'coll.html')