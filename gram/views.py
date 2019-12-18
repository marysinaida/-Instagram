from django.shortcuts import render
from django.http  import HttpResponse



# Create your views here.

def signUp(request):
    return render(request,'registration/registration_form.html')

def login(request):
    return render(request,'registration/login.html')

def home(request):

    return render(request,'index.html')
