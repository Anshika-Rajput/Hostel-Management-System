from datetime import datetime
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import contact_us
# Create your views here.
def studentHome(request):
    
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist:)')
                print('email already exist')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(username=email, password=password1, email=email, first_name=name)
                user.save()
                return redirect('/login/')
                
        else:
            messages.info(request, "Passowrd didn't match:(")
            return redirect('/signup/')

    else:

        return render(request, 'signup.html')

def facilities(request):
    return render(request, 'facilities.html')
        
def contactus(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']

        b = contact_us(name=name, email=email, message=message)
        b.save()
        forms = contact_us.objects.all()
        context={'forms':forms}
        return redirect('/contactus/')
    

    else:
        return render(request, 'contactus.html')
def pricing(request):
    return render(request, 'pricing.html')


    

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('/login/')


    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')