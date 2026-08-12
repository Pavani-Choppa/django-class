from django.shortcuts import render

# Create your views here.

def home(request):
    name="Gayathri"
    products = [
        {"name":"Mobile","price":20000},
        {"name":"Laptop", "price": 120000},
        {"name":"Bike", "price": 160000},
    ]
    numbers = [10,11,12,13,14,15,16,17,18,19,20]
    n1 =  10
    n2 = 11
    return render(request,'base.html',context={"name":name,
                                                           "products":products,
                                                           "numbers":numbers,
                                                           "n1":n1,
                                                           "n2":n2})