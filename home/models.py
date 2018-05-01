from django.db import models
from django.utils import timezone

# Create your models here.
class itemFood(models.Model):
    chefId = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptionShort=models.CharField(max_length=50)
    descriptionLong=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    featured=models.BooleanField(default=True)
    showItem=models.BooleanField(default=True)
    image_1=models.FileField(null=True, blank=True)
    image_2=models.FileField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        info=str(self.id)+" "+self.title
        return info
class personalInfo(models.Model):
    chefName = models.CharField(max_length=30,blank=True,null=True)
    about = models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    chefId = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message=models.CharField(max_length=50,null=True)
    def __str__(self):
        pinfo=str(self.id)+" "+self.chefName
        return pinfo

