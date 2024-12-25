from django.shortcuts import render

# Create your views here.


# a sample home funcion to load home page
def home(request):
    return render(request,'home.html')