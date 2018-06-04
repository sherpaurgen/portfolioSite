from django import forms
from django.forms import ModelForm,Textarea
from home.models import ItemFood,userInfo
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminFileWidget


class createItemForm(ModelForm):
    image_1=forms.ImageField(widget=AdminFileWidget)
    class Meta():
        model=ItemFood
        exclude = ['created_date','user']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 2}),
        }


class userRegistrationForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','is_active',)


class UserInfoForm(ModelForm):
    profile_pic1=forms.ImageField(widget=AdminFileWidget,required=False)
    profile_pic2=forms.ImageField(widget=AdminFileWidget,required=False)
    class Meta():
        model = userInfo
        fields = ('chefName', 'about', 'phone', 'address', 'email', 'message', 'profile_pic1', 'profile_pic2')
        widgets = {
            'message': Textarea(attrs={'cols': 50, 'rows': 2}),
        }