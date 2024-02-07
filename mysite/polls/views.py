from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Customer
from .models import Employee
def polls(request):
    return render(request, 'polls/login.html')

def home(request):
  template = loader.get_template('polls/Home.html')
  return HttpResponse(template.render())

def login(request):
    return render(request, 'polls/login.html')

def elogin(request):
    return render(request, 'polls/LoginEmp.html')
def EmpLogin(request):
    return render(request, 'polls/LoginEmp.html')
def buy(request):
    return render(request, 'polls/buy.html')
def service(request):
    return render(request, 'polls/service.html')
    
def events(request):
    return render(request, 'polls/events.html')
def chome(request):
    return render(request, 'polls/eafter.html')
def ehome(request):
    return render(request, 'polls/empafter.html')





def loginverify(request):
    print("-----------login verification------------")
    if request.method == "POST":
        cemail = request.POST.get("cemail")
        cpassword = request.POST.get('cpassword')
        print(cemail, cpassword)
        all_customers = Customer.objects.all()

    # Print the users (for debugging purposes)
        elist,epass=[],[]
        for customer in all_customers:
            elist.append(customer.Email)
            epass.append(customer.password)
            print(customer.Email,customer.password)
        n=elist.index(cemail)
        m=epass.index(str(cpassword))
        print(elist,epass)
        if n == m:
            user = authenticate(request,Email=cemail,password=cpassword)
            login(user)
            print("no problem")
            messages.success(request, 'Login customer successful')
            messagess = True
            redirect_url = '/chome/'
            return JsonResponse({'redirect_url': redirect_url})
        else:
            messages.error(request, 'Invalid email or password')
            print("problem occurred")

            redirect_url = '/Registration/'
            return JsonResponse({'redirect_url': redirect_url})  # Redirect to login page
    template = 'polls/CustLandingpage.html'
    return render(request, template)
# def emploginverify(request):
#     print("----------- Emplogin verification------------")
#     if request.method == "POST":
#         eemail = request.POST.get("eemail")
#         epassword = request.POST.get('epassword')
#         print(eemail, epassword)
#         all_employee = Employee.objects.all()
#         elist,epass=[],[]
#         for Employee in all_employees:
#             elist.append(Employee.Email)
#             epass.append(Employee.password)
#             print(Employee.Email,Employee.password)
#         n=elist.index(eemail)
#         m=epass.index(str(epassword))
#         print(elist,epass)
#         if n == m:
#             user = authenticate(request,Empemail=eemail,Emppassword=epassword)
#             print(user)
#             login(request, user)
#             print("no problem")
#             messages.success(request, 'Login  emp successful')
#             messagess = True
#             redirect_url = '/ehome/'
#             return JsonResponse({'redirect_url': redirect_url})
#         else:
#             messages.error(request, 'Invalid email or password')
#             print("problem occurred")
#             redirect_url = '/EmpR/'
#             return JsonResponse({'redirect_url': redirect_url})  
#     template = 'polls/CustLandingpage.html'
#     return render(request, template)

def emploginverify(request):
    print("----------- Emplogin verification------------")
    if request.method == "POST":
        eemail = request.POST.get("eemail")
        epassword = request.POST.get('epassword')
        print(eemail, epassword)
        all_employees = Employee.objects.all()  # Corrected variable name
        elist, epass = [], []
        for employee in all_employees:  # Corrected variable name
            elist.append(employee.Empemail)
            epass.append(employee.Emppassword)
            print(employee.Empemail, employee.Emppassword)
        try:
            n = elist.index(eemail)
            m = epass.index(str(epassword))
            print(elist, epass)
            if n == m:
                user = authenticate(request, Empemail=eemail, Emppassword=epassword)
                print(user)
                login(user)
                print("no problem")
                messages.success(request, 'Login  emp successful')
                messagess = True
                redirect_url = '/ehome/'
                return JsonResponse({'redirect_url': redirect_url})
            else:
                messages.error(request, 'Invalid email or password')
                print("problem occurred")
                redirect_url = '/EmpR/'
                return JsonResponse({'redirect_url': redirect_url})  
        except ValueError:
            messages.error(request, 'Invalid email or password')
            print("problem occurred")
            redirect_url = '/EmpR/'
            return JsonResponse({'redirect_url': redirect_url})  

    template = 'polls/CustLandingpage.html'
    return render(request, template)

def Registration(request):
    return render(request, 'polls/Crregis.html')

def EmpRegistration(request):
    return render(request, 'polls/EmpRegia.html')
  
# def EmpRegistration(request):
#     template = loader.get_template('polls/EmpReg.html')
#     return HttpResponse(template.render())


  
def defaultpg(request):
    print("-----------challa  bagh------------")
    if request.method == "POST":
        # Use request.POST.get() to retrieve form data
        name = request.POST.get("name")
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        new_cus = Customer(name=name,Email=email,password=password)
        new_cus.save()
        
        template = loader.get_template('polls/EmpLogin.html')
        return HttpResponse(template.render())
        

   

    # You may want to handle the case when the request method is not POST
    template = loader.get_template('polls/EmpLogin.html')
    return HttpResponse(template.render())


def emphome(request):
    print("-----------Page worked------------")
    if request.method == "POST":
        # Use request.POST.get() to retrieve form data
        name = request.POST.get("name")
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        new_emp = Employee(Empname=name,Empemail=email,Emppassword=password)
        new_emp.save()
        template = loader.get_template('polls/EmpLogin.html')
        return HttpResponse(template.render())
        

   

    # You may want to handle the case when the request method is not POST
    template = loader.get_template('polls/EmpLogin.html')
    return HttpResponse(template.render())
def hi(request):
        return render(request, 'polls/EmpReg.html')

    
   

