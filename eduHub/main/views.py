from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import Subject
from main.models import Data

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('')

        if password != confirm_password:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(
            request, "Your Account has been created succesfully!!")
        return redirect('signIn')

def signIn(request):
    return render(request,'login.html')

def loginAction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.error(request, 'Sucessfully Logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signIn')

    return redirect('register')

def home(request):
    user = request.user
    subjects = Subject.objects.all().filter(u_name=user.username)
    return render(request,'home.html',{'subjects': subjects})

def homepg(request):
    user = request.user
    subjects = Subject.objects.all().filter(u_name=user.username)
    return render(request,'home.html',{'subjects': subjects})

def subject(request,sname):
    topics = Data.objects.all().filter(subject_name=sname)
    return render(request,'subject.html',{'topics':topics})

def profile(request):
    user = request.user
    subjects = Subject.objects.all().filter(u_name=user.username)
    return render(request,'profile.html',{'subjects': subjects})

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signIn')

def delete(request, topic):
  topic = Data.objects.get(topic_name=topic)
  topic.delete()
  return render(request,'subject.html')
