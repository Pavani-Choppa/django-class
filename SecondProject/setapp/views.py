from django.http import HttpResponse

def add_method(request):
    s = {10, 20, 30}
    s.add(40)

    return HttpResponse(s)

def update_method(request):
    s = {10, 20}
    s.update([30, 40])

    return HttpResponse(s)


def pop_method(request):
    s = {10, 20, 30}

    s.pop()

    return HttpResponse(s)

def remove_method(request):
    s = {10, 20, 30}

    s.remove(20)

    return HttpResponse(s)