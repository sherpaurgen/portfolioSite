from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from home.models import ItemFood,userInfo
from home.forms import createItemForm,UserInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login,logout
owner="Urgen Sherpa"

def index(request):
    activeItems=ItemFood.objects.filter(featured=True,showItem=True)[0:6]
    motto=userInfo.objects.all().last().message
    my_dict={'homepage_title':"Gordon Ramsey", 'activeItems':activeItems,'motto':motto,'owner':owner}
    return render(request,'home/index.html',my_dict)

def recipy(request):
    activeItems=ItemFood.objects.filter(featured=True,showItem=True)[0:6]
    my_dict={'homepage_title':"Gordon Ramsey", 'activeItems':activeItems,'owner':owner}
    return render(request,'home/recipe.html',my_dict)

def about(request):
    about = userInfo.objects.all().last().about
    print(about)
    return render(request,'home/about.html',{'about':about,'owner':owner})

def contact(request):
    ChefName=userInfo.objects.all().last().chefName
    Email=userInfo.objects.all().last().email
    Phone=userInfo.objects.all().last().phone
    return render(request,'home/contact.html',{'PageTitle':"Contact Me", 'ChefName':ChefName,"Email":Email,"Phone":Phone,'owner':owner})

@login_required(login_url='/login')
def createItemView(request):
    if request.method == 'POST':
        form=createItemForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            print("create food form saved!!")
    form = createItemForm
    return render(request, 'home/create.html', {'form':form, 'owner':owner})

@login_required(login_url='/login')
def ManageProfile(request):
    if request.method=="POST":
        form=UserInfoForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            status="Information saved"
    form = UserInfoForm
    status=None
    return render(request,'home/edituser.html',{'form':form,'status':status})


def signup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid")
            return redirect('/login')
    else:
        form=UserCreationForm()
    return render(request,'home/signup.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                print(user)
                auth.login(request, user)
                return redirect('/manage/')
    else:
        form = AuthenticationForm()
    return render(request,'home/login.html',{'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    else:
        logout(request)
        return redirect('/')
