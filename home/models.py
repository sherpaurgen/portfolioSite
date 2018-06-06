from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ItemFood(models.Model):
    user = models.ForeignKey(User,default=None)
    title = models.CharField(max_length=100)
    description=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    featured=models.BooleanField(default=True)
    showItem=models.BooleanField(default=True)
    image_1=models.ImageField(upload_to='media/%Y/%m/%D/',null=True, blank=True)
    image_2=models.ImageField(upload_to='media/%Y/%m/%D/',null=True, blank=True)
    def __str__(self):
        return self.title

class userInfo(models.Model):
    #create relationship
    user=models.ForeignKey(User,default=None)
    #additional
    chefName = models.CharField(max_length=30,blank=True,null=True)
    about = models.CharField(max_length=500,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    message = models.CharField(max_length=50,null=True)
    profile_pic1 = models.ImageField(upload_to='media/%Y/%m/%D/', blank=True,null=True)
    profile_pic2 = models.ImageField(upload_to='media/%Y/%m/%D/', blank=True, null=True)
    def __str__(self):
        return self.chefName


