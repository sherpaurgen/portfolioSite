from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from home.models import ItemFood,userInfo
from home.forms import createItemForm,UserInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login,logout
from django.views.generic import ListView, DetailView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    try:
        activeItems=ItemFood.objects.filter(featured=True,showItem=True)[0:6]
        motto=userInfo.objects.all().last().message
        videoUrl=userInfo.objects.all().last().channelUrl
        profileDetail=userInfo.objects.all().last().profileDetail
        showcaseimage1=userInfo.objects.all().last().showcaseimage1
        showcaseimage2 = userInfo.objects.all().last().showcaseimage2
        showcaseimage3 = userInfo.objects.all().last().showcaseimage3
        my_dict={'activeItems':activeItems,'motto':motto,'videoUrl':videoUrl,'profileDetail':profileDetail,'carouselimg1':showcaseimage1,'carouselimg2':showcaseimage2,'carouselimg3':showcaseimage3}
    except:
        my_dict={}
    return render(request,'home/index.html',my_dict)

# def recipy(request):
#     activeItems=ItemFood.objects.filter(featured=True,showItem=True)[0:6]
#     my_dict={'homepage_title':"Gordon Ramsey", 'activeItems':activeItems}
#     return render(request,'home/recipe.html',my_dict)

def about(request):
    try:
        aboutme = userInfo.objects.all().last().about
        aboutImg= userInfo.objects.all().last().profile_pic1
        mydict={'about':aboutme,'aboutImg':aboutImg}
    except:
        mydict={}
    return render(request,'home/about.html',mydict)

def contact(request):
    try:
        print("in try section")
        ChefName=userInfo.objects.all().last().chefName
        Email=userInfo.objects.all().last().email
        Phone=userInfo.objects.all().last().phone
        contactImg = userInfo.objects.all().last().profile_pic2
        mydict={'PageTitle':"Contact Me", 'ChefName':ChefName,"Email":Email,"Phone":Phone,"contactImg":contactImg}
    except:
        mydict={}
    print("value of ",mydict)
    return render(request,'home/contact.html',mydict)

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
    return render(request, 'home/create.html', {'form':form})

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
                return redirect('/')
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

class showItem(ListView):
    template_name = 'home/recipe.html'
    context_object_name = "items"
    model = ItemFood
    paginate_by = 6

def manageFeatured(request):
    try:
        FeaturedItems=ItemFood.objects.filter(featured=True,showItem=True)
        my_dict={'items':FeaturedItems}
    except:
        my_dict={}
    return render(request,'home/featured.html',my_dict)

class itemDetail(DetailView):
    template_name='home/itemdetail.html'
    model = ItemFood

@login_required(login_url='/login')
def itemUpdateView(request,pk):
    data = get_object_or_404(ItemFood,pk=pk)
    if request.method == 'POST':
        form=createItemForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            updinstance=form.save(commit=False)
            updinstance.user=request.user
            updinstance.save()
            return redirect(data.get_absolute_url())
            #return redirect('/itemDetail/{}'.format(data.pk))
    form = createItemForm(instance=data)
    return render(request, 'home/create.html', {'form':form})

@login_required(login_url='/login')
def ManageProfile(request):
    print(request.user," id is ")
    pk=request.user.id
    print(request.user.id)
    try:
        data = get_object_or_404(userInfo, pk=pk)
        if request.method == "POST":
            form=UserInfoForm(request.POST,request.FILES,instance=data)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.user=request.user
                instance.save()
                status="Information saved"
        form = UserInfoForm(instance=data)
        return render(request,'home/edituser.html',{'form':form})
    except:
        if request.method == "POST":
            form = UserInfoForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                status = "Information saved"
        form = UserInfoForm()
        return render(request, 'home/edituser.html', {'form': form})

class itemDeleteView(LoginRequiredMixin,DeleteView):
    model = ItemFood
    success_url = reverse_lazy("showItem")

