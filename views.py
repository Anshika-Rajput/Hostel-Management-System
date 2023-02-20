from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from .models import Booking
from student.models import contact_us
# Create your views here.
def managementHome(request):
    
    return render(request, 'management.html')


def contact_forms(request):
    forms=contact_us.objects.all()
    context={'forms':forms}
    return render(request, 'contact_forms.html', context)
    






def student_list(request):
    if request.method == 'POST':
        # For Adding the booking

        name = request.POST['name']
        email = request.POST['email']
        room_no = request.POST['room_no']
        new_booking = Booking(name = name, email = email, room_no = room_no)
        new_booking.save()
        return redirect('/management/student_list/')

        
    

    else:
        booking_list = Booking.objects.all()
        book_list=[]
        for i in booking_list:
            book_list.append(i)
        context={'booking_list' : book_list}

        return render(request, 'studentlist.html',context)

def remove_booking(request):
    if request.method == 'POST':
        # For Deleting the booking
        emails = request.POST['remove_email']
        forms = Booking.objects.all()
        for i in forms:
            
            if emails == i.email:
                print(i.email)
                i.delete()
        return redirect('/management/student_list/')
    
    else:
        return redirect('/management/student_list/')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_superuser:
            auth.login(request, user)
            return redirect('/management/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('/management/login')

    else:
        return render(request, 'management_login.html')

def logout(request):
    auth.logout(request)
    return redirect('/management/')