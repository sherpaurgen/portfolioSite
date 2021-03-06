from django import forms
from django.forms import ModelForm,Textarea
from home.models import ItemFood,userInfo
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminFileWidget


class createItemForm(ModelForm):
    # image_1=forms.ImageField(widget=AdminFileWidget)
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
        fields = ('chefName', 'about','profileDetail', 'phone', 'address', 'email', 'message','channelUrl', 'profile_pic1', 'profile_pic2','showcaseimage1','showcaseimage2','showcaseimage3','ytlink','fblink','instalink')
        widgets = {
            'message': Textarea(attrs={'cols': 50, 'rows': 2}),
            'profileDetail': Textarea(attrs={'cols': 50, 'rows': 2}),
            'about': Textarea(attrs={'cols': 50, 'rows': 2}),
        }
        help_texts = {'showcaseimage1':'try to upload image with 1900x1080 resolution',
                      'showcaseimage2': 'try to upload image with 1900x1080 resolution',
                      'showcaseimage3': 'try to upload image with 1900x1080 resolution',
                      'channelUrl': 'eg. https://www.youtube.com/embed/tgbNymZ7vqY',
                      'fblink': 'Facebook page link here eg. https://www.facebook.com/zuck',
                      'ytlink': 'Enter youtube channel or video here',
                      'instalink': 'Enter your instagram page'
                      }