from django.shortcuts import redirect, render
from django.http import HttpResponse
from app import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def package(request):
    packages = Packages.objects.all()


    return render(request,'package.html' , {'packages':packages})
def blog(request):
    return render(request,'blog.html')  
def testimonial(request):
    return render(request,'testimonial.html')
def destination(request):
    destinations = Destination.objects.all()
    return render(request, 'destination.html', {'destinations': destinations})
def contact(request):
    return render(request,'contact.html')
def team(request):
    return render(request,'team.html')
def base(request):
    return render(request,'base.html')
def register(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm-password')
        if password==confirmpassword:
            user = CustomUser(name=name, email=email, password=password)
            user.save()
            return redirect('login')


    return render(request,'register.html')
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = CustomUser.objects.get(email=email)
        if user:
            if password==user.password:
                return redirect('index')

    return render(request,'login.html')

def subpackage(request, package_id):
    list_package = SubPackage.objects.filter(package = package_id)
    print(list_package[0])
    return render(request,'subpackage.html', {'list_package':list_package})