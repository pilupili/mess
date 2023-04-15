from django.shortcuts import render,redirect
from signin.models import Register,UploadImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lg,logout as lgt
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'sign-in/index.html')

@login_required
def logout(request):
    lgt(request)
    return redirect('login')
@login_required
def update(request):
    user2=User.objects.get(email=request.user.email)
    user2.first_name = request.POST.get("first_name")
    user2.last_name = request.POST.get("last_name")
    print(request.POST.get("password"))
    # if request.POST.get("password") != '' or request.POST.get("password") is not None :
    #     user2.set_password(request.POST.get("password"))
    
    user2.save()
    im=UploadImage()
    if len(request.FILES) != 0:
        im.image = request.FILES['Image']
    im.save()    
        

    return redirect('sidebar')


@login_required
def profile(request):
    print(type(request.user.email))
    user1=User.objects.filter(email = request.user.email)
    print(user1)
    user_obj={}
    for temp in user1:
        print(temp.first_name)
        user_obj['first_name'] = temp.first_name
        user_obj['last_name'] = temp.last_name
    return render(request,'profile/index.html',user_obj)

def signin(request):    
    EMAIL = request.POST.get("email")
    pwd = request.POST.get("password")
    print(EMAIL)
    user = authenticate(username=EMAIL,password=pwd)
    if User.objects.filter(username = EMAIL).exists():
        if user is not None:
            lg(request,user)
            return redirect('sidebar')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')   
    return render(request,'sign-in/index.html')

@login_required
def sidebar(request):
    print(request.user)
    print("is user authenticated" + str(request.user.is_authenticated))
    # if not (request.user.is_authenticated):
    #    print("Redirecting to the home page")
    #    return redirect('login')
    return render(request,'sidebars/index.html')




def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        EMAIL = request.POST.get("email")
        pwd = request.POST.get("password")
        if User.objects.filter(username = EMAIL).exists():
            messages.info(request,'email is already registered.Register with a new email-id')
            return redirect('register')
        else:
            register1 = User(first_name=first_name,last_name=last_name,username=EMAIL,email=EMAIL,password=pwd)
            register1.set_password(pwd)
            register1.save()
            return redirect('login')
    return render(request,'sign-in/register.html')
