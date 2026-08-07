from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        opertaion = request.POST.get("operation")
        res = 0
        if opertaion == "add":
            res = num1 + num2
        elif opertaion == "mul":
            res = num1 * num2
        elif opertaion == "power":
            res = num1 ** num2
        return  render(request,'home.html',context={'num1':num1,'num2':num2,'res':res})
        # print(res)
        # print(num1,num2,opertaion)
    return render(request, 'home.html')