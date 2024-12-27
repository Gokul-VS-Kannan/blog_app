from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


# a sample home funcion to load home page
def home(request):
    return render(request,'home.html')

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
