from django.http import HttpResponse

def sample(request):
    return HttpResponse("Welcome to Conditions")

def html_fun(request):
    return HttpResponse("<h3>Welcome to html class</h3>")

def css_fun(request):
    return HttpResponse("<h1 style = 'color : green '>Welcome to css class</h1>")

def biggest(request,a,b,c):
    if a > b and a > c:
        return HttpResponse(f"<h1>{a} is Biggest Number </h1>")
    elif b > a and b > c:
        return HttpResponse(f"<h1>{b} is Biggest Number </h1>")
    else:
        return HttpResponse(f"<h1>{c} is Biggest Number </h1>")


def smallest(request,a,b,c):
    if a < b and a < c:
        return HttpResponse(f"<h1>{a} is smallest Number </h1>")
    elif b < a and b < c:
        return HttpResponse(f"<h1>{b} is smallest Number </h1>")
    else:
        return HttpResponse(f"<h1>{c} is smallest Number </h1>")

def even(request,n):
    if n % 2 == 0:
        return HttpResponse(f"<h1>Yes,{n} is even Number</h1>")
    else:
        return HttpResponse(f"<h1>No,{n} is Not Even Number</h1>")

def odd(request,n):
    if n % 2 != 0:
        return HttpResponse(f"<h1>Yes, {n} is odd Number</h1>")
    else:
        return HttpResponse(f"<h1>No, {n} is Not Odd Number</h1>")