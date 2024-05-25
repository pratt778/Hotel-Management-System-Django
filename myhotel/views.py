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
    data={}
    myfac = Facility.objects.all()
    myhotel = Hotel.objects.all()
    user = request.user
    frmt='REC'

    if request.method == 'GET':
        if 'find' in request.GET:
            frmt = request.GET.get('sort_by')
            search= request.GET.get('search')
            facilities = request.GET.getlist('facilities')
            print(facilities)
            if frmt=='ASC':
                myhotel = myhotel.order_by('hotel_price')
               
            elif frmt=='DESC':
                myhotel = myhotel.order_by('-hotel_price')

            myhotel = myhotel.filter(hotel_name__icontains=search)
            print(myhotel)
            if len(facilities):
                myhotel = myhotel.filter(facility__facility_name__in=facilities).distinct()
                print(myhotel)
    data={
        'user':user,
        'facility':myfac,
        'hotels':myhotel,
        'sort':frmt
    }
    return render(request,'home.html',data)


def out(request):
    logout(request)
    return redirect('login')

@login_required
def hoteldetail(request,uid):
    msg=''
    myhotel = Hotel.objects.get(uid=uid)
    if request.method == 'POST':
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        print(check_in)
        print(check_out)
        mybooking = HotelBooking.objects.create(hotels=myhotel,user=request.user,start_date=check_in,end_date=check_out,booking_type='Pre Paid')
        if mybooking is not None:
            mybooking.save()
            msg='Booking Successful'
    return render(request,'details.html',{'hotel':myhotel,'msg':msg})