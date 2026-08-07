from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    return render(request,'home.html')

def display_data(request):
    # s_name = request.GET.get('name')
    # s_age = request.GET.get('age')
    # s_place = request.GET.get('place')
    # s_mobile = request.GET.get('mobile')
    # s_blood = request.GET.get('blood_group')
    # skills = request.GET.getlist('skills')
    # s_skills = ", ".join(skills)
    s_name = request.POST.get('name')
    s_age = request.POST.get('age')
    s_place = request.POST.get('place')
    s_mobile = request.POST.get('mobile')
    s_blood = request.POST.get('blood_group')
    skills = request.POST.getlist('skills')
    s_skills = ", ".join(skills)

    # print(s_name)
    # print(s_age)
    # print(s_place)
    # print(s_mobile)
    # print(s_blood)
    # print(s_skills)

    s_data = {'s_name':s_name,'s_age':s_age,'s_place':s_place,'s_mobile':s_mobile,'s_blood':s_blood,'s_skills':s_skills}
    return render(request,'display.html',s_data)

    # return HttpResponse(s_data)