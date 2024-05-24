from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Hotel,HotelBooking,Facility

# Create your views here.
def signup(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        passw = request.POST['passw']
        conpass = request.POST['cpassw']
        myuser = User.objects.create_user(username=name,email=email,password=passw)
        if myuser is not None:
            myuser.save()
            return redirect('login') 

    return render(request,'signup.html')

def log(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        myuser = authenticate(username=uname,password=passw)
        if myuser is not None:
            login(request,myuser)
            return redirect('home')
    return render(request,'login.html')

@login_required
def home(request):
    myfac = Facility.objects.all()
    myhotel = Hotel.objects.all()
    user = request.user
    data={
        'user':user,
        'facility':myfac,
        'hotels':myhotel
    }
    return render(request,'home.html',data)


def out(request):
    logout(request)
    return redirect('login')