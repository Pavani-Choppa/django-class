from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')

def display(request):
    return render(request,'display.html')

def about(request):
    return render(request,'about.html')