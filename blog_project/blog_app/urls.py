from django.urls import path
# importing view file
from . import views




urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('welcome',views.welcome,name='welcome'),
]