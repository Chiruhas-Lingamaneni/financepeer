from django.shortcuts import render,redirect
from user_app.forms import CreateUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@user_passes_test(lambda user: not user.username, login_url='/home', redirect_field_name=None)
def registerpage(request):
    form=CreateUserForm()
    registered=False
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            registered=True

    context={'form':form,'registered':registered}
    return render(request,'user_app/register.html',context)

@user_passes_test(lambda user: not user.username, login_url='/home', redirect_field_name=None)
def loginpage(request):
    cradestials=False
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            cradestials=True
    return render(request,'user_app/login.html',{'cradentials':cradestials})



