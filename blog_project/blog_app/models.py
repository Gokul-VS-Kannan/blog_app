from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


# create models for blog

class BlogPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name='user_blog')
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # get_user_full_name method will combine first_name and last_name in user table
    def get_user_full_name(self):
        return self.user.get_full_name()  
    
    def get_user_username(self):
        return self.user.username 