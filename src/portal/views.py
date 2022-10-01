from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        candidate = Candidate.objects.filter(company__user=request.user)
        context={
            'candidate': candidate
        }
        return render (request, 'jobseeker.html', context)
    else:
         company = Company.objects.all()
         context={
             'company':company,
         }
         return render(request,'hr.html',context)

def loginUser(request):
    if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect ('home')
            else:
                messages.info(request, 'Invalid Username or Password')
                return redirect('login')
           
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'login.html')


def signup(request):
        if request.user.is_authenticated:
             return redirect('home')
        else:
            form = CustomUserCreationForm() 

            
            if request.method == "POST":
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.info(request,'Account created successfully')

                    return redirect('login')   
        context={
            'form':form
            }
        return render(request,'sign_up.html',context)

def applyPage(request,id):
    company = Company.objects.get(id=id)
    form=CandidateForm()
    if request.method=='POST':
        form=CandidateForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'apply.html',context)

def jobposting(request):
    form = CompanyForm()
    post= Company.objects.all()
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form, 'post':post}
    return render(request,'jobposting.html',context)