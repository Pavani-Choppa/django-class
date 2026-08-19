from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')


def event(request):
    return render(request,'event.html')


def menu(request):
    return render(request,'menu.html')


def contact(request):
    return render(request,'contact.html')


def book(request):
    return render(request,'book.html')


def blog(request):
    return render(request,'blog.html')


def team(request):
    return render(request,'team.html')


def dis_404(request):
    return render(request,'404.html')