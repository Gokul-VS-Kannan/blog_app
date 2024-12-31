from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

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
    blog=BlogPost.objects.all()

    return render(request,'loginhome.html'{'blog':blog})

@login_required
def profile(request):
    # check the user is authenticted if not redirect to login
    if not request.user.is_authenticated:
        return redirect('login_view')
    # fetching the data of loged in user from User table
    user=User.objects.get(username=request.user.username)
    blog=BlogPost.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user': user,'blog':blog})

@login_required
def blogform(request):
    form=BlogPostForm
    return render(request,'add_blog.html',{'form':form})

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)# the commit is set false because user is not set mannualy though the form
            blog.user = request.user  
            blog.save()
            return redirect('profile')
        else:
            form = BlogPostForm()
            return render(request, 'add_blog.html', {'form': form})


#function to display the form with existing content and updte it
@login_required
def edit_blog(request,blog_id):
    blog = BlogPost.objects.get(id=blog_id,user=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = BlogPostForm(instance=blog)

    return render(request,'edit_blog.html',{'form':form, 'blog':blog})

# function to delete blog
@login_required
def delete_blog(request,blog_id):
    blog = BlogPost.objects.get(id=blog_id,user=request.user)

    # delete the blog
    blog.delete()

    return redirect('profile')

# function to view blogs
@login_required
def blog_view(request,blog_id):
    blog=BlogPost.objects.get(id=blog_id)
    return render(request,'blog_view.html',{'blog':blog})

