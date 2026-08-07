from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome To While Loops")

def prime(request,n):
    i = 2
    if n <= 1:
        return HttpResponse(f"<h1>The number {n} is Not prime Number</h1>")
    else:
        while i < n :
            if n % 2 == 0:
                return HttpResponse(f"<h1>The number {n} is NOt prime Number</h1>")
            i += 1
        else:
            return HttpResponse(f"<h1>The number {n} is prime Number</h1>")


def armstrong(request ,n):
    num = len(str(n))
    res = n
    arm = 0
    while n > 0:
        rem = n % 10
        arm += rem ** num
        n //= 10
    if res == arm:
        return HttpResponse(f"<h1> {res} is an ArmStrong Number </h1>")
    else:
        return HttpResponse(f"<h1> {res} is Not an ArmStrong Number </h1>")


def palindrome(request,n):
    num = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev*10 + rem
        n //= 10
    if num == rev:
        return HttpResponse(f"<h1 style='color:green'> {num} is a Palindrome Number </h1>")
    else:
        return HttpResponse(f"<h1 style='color:red'>{num} is not a palindrome Number </h1>")

def str_palindrome(request,s):
    rev = ''
    for i in s:
        rev = i+rev
    if s == rev:
        return HttpResponse(f"<h1 style='color:green'> {s} is a Palindrome String </h1>")
    else:
        return HttpResponse(f"<h1 style='color:red'> {s} is not a Palindrome String </h1>")