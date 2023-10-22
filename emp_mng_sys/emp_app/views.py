
from django.shortcuts import render, HttpResponse, redirect
from .models import Employee
from django.db.models import Max
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
        }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        new_emp = Employee(first_name = first_name, last_name = last_name, email = email, phone = phone)
        new_emp.save()
        print('Employee added successfully')
        return redirect("/")
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occured! Employee Has not Added')
    

def remove_emp(request,empid = 0):
    if empid:
        try:
            emp_to_be_removed = Employee.objects.get(id=empid)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please enter a valid emp id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
        }
    return render(request, 'remove_emp.html', context)

def edit_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
        }
    print(context)
    return render(request,'edit_emp.html',context)

def update_emp(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,'update.html',{'emp':emp})

def uprec(request,id):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    phone=request.POST['phone']
    emp=Employee.objects.get(id=id)
    emp.first_name=first_name
    emp.last_name=last_name
    emp.email=email
    emp.phone=phone
    emp.save()
    return redirect("/")