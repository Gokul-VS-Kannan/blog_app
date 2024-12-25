from django.urls import path
# importing view file
from . import views




urlpatterns=[
    path('',views.home,name='home')
]