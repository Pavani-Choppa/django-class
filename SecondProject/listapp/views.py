from django.http import HttpResponse


def append_method(request):
    li = [10, 20, 30]
    li.append(40)

    return HttpResponse(li)

def extend_method(request):
    li = [10, 20]
    li.extend([30, 40, 50])

    return HttpResponse(li)

def pop_method(request):
    li = [10, 20, 30, 40]
    li.pop()

    return HttpResponse(li)

def remove_method(request):
    li = [10, 20, 30, 40]
    li.remove(20)

    return HttpResponse(li)