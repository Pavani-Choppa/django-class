from django.http import HttpResponse

def odd_list(request):
    numbers = [2, 5,7,9,4, 6, 8, 10]
    odd = []
    for i in numbers:
        if i % 2 != 0:
            odd += [i]
    return HttpResponse(f"Odd Numbers Of {numbers} : is {odd}")

def odd_sum(request):
    numbers = [2, 5,7,9,4, 6, 8, 10]
    sum = 0
    for i in numbers:
        if i % 2 != 0:
            sum += i
    return HttpResponse(f"Sum of {numbers} : is {sum}")
