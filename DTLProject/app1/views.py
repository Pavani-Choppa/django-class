from django.shortcuts import render

# Create your views here.
def home(request):
    x = 10
    y = 20
    student_names = ["pavani","Gayathri","Uma","Mohith","Pavi"]
    student_data = [['bhavana','gayathi','lavanya'],[100,95,90]]
    employee_data = [{'name':'pavvu','age':20},{'name':'Gayi','age':19}]

    context = {'n1':x,'n2':y,'sn':student_names,'sd':student_data,'ed':employee_data}

    return render(request,'index.html',context)