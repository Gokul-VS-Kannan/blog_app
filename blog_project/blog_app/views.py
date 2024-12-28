from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# a sample home funcion to load home page
def home(request):
    return render(request,'home.html')

# login
def login_view(request):
    # login querry
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        # authenticte the user
        user = authenticate(request,username=username,password=password)

        # check if user exist or not
        if user is not None:
            # if exist then login
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request,'home.html')


# logout
def logout_view(request):
    logout(request)
    return redirect('home')


# a function for registration purpose
def register(request):
    # check the method of form if it is post
    if request.method=="POST":
        # get the value that an user provide
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pwd']
        confirm_password = request.POST['cpwd']

        # Check if passwords match 
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request,'registration.html')
            
        # Check if username is already taken or not 
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request,'registration.html')
            

         # Check if email is already registered or not
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request,'registration.html')

        # if all the conditions are fullfilled then save the user details and redirect to login page

        # create an user instance object
        user=User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

        # Hash the password before saving for login
        user.set_password(password)

        # save the user instance object
        user.save()
        return redirect('home')

    return render(request, 'registration.html')

# a simple function for displaying welcome page after login
@login_required
def welcome(request):
    return render(request,'loginhome.html')
