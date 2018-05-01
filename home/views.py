from django.shortcuts import render
# Create your views here.
from home.models import itemFood,personalInfo
owner=personalInfo.objects.values('chefName').get(id=1)

def index(request):
    activeItems=itemFood.objects.filter(featured=True,showItem=True)
    motto=personalInfo.objects.values('message').get(id=1)
    my_dict={'homepage_title':"Gordon Ramsey",'activeItems':activeItems,'motto':motto,'owner':owner}
    print(my_dict)
    return render(request,'home/index.html',context=my_dict)

def contact(request):
    user=personalInfo.objects.values_list('address','phone','email').get(pk=1)
    my_dict={'homepage_title':"Contact Me",'user':user,'owner':owner}
    return render(request,'home/contact.html',context=my_dict)
