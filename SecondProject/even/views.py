from django.http import HttpResponse

def even_list(request):
    numbers = [2, 5,7,9,4, 6, 8, 10]
    even = []
    for i in numbers:
        if i % 2 == 0:
            even += [i]
    return HttpResponse(f"Even Numbers Of {numbers} : is {even}")

def even_sum(request):
    numbers = [2, 5,7,9,4, 6, 8, 10]
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return HttpResponse(f"Sum of {numbers} : is {sum}")
