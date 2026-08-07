from django.http import HttpResponse

def home_fun(request):
    return HttpResponse("My first Django project")

# def home_fun():
#     return None