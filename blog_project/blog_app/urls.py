from django.urls import path
# importing view file
from . import views




urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('welcome',views.welcome,name='welcome'),
    path('profile',views.profile,name='profile'),
    path('blogform',views.blogform,name='blogform'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('edit_blog/<int:blog_id>',views.edit_blog,name='edit_blog'),
    path('delete_blog/<int:blog_id>',views.delete_blog,name='delete_blog'),
    path('blog_view/<int:blog_id>',views.blog_view,name='blog_view'),
    path('search/',views.search_blog,name="search"),
]