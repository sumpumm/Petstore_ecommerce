from django.shortcuts import render


def HomePage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
