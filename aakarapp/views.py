from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount

## import data tables from database
from .models import Submission


# Create your views here.


def registerLogiq(request):
    return render(request, "submission.html")

def index(request):
    user = request.user
    is_filled = False 
    if user.is_authenticated:
        email = user.email
        is_filled = len(Submission.objects.filter(email=email))==1
    print(is_filled)

    return render(request, "index.html",
    {
        'is_filled':is_filled
    })

def logiq(request):
    user = request.user
    is_filled = False 
    if user.is_authenticated:
        email = user.email
        is_filled = len(Submission.objects.filter(email=email))==1
    return render(request, "logiq.html",
    {
        'is_filled':is_filled
    })


def submitted(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name', '')
        email = user.email
        colgName = request.POST.get('colgName', '')
        branch = request.POST.get('branch', '')
        mobileNo = request.POST.get('mobileNo', '')
        # mail = request.POST.get('mail', '')
        program = request.POST.get('program', '')
        year = request.POST.get('year', '')
        address = request.POST.get('address', '')
        roll_no = request.POST.get('roll_no', '')

        response = Submission(name=name, email=email, colgName=colgName,  branch=branch, mobileNo=mobileNo,
                              year=year, roll_no=roll_no, address=address, program=program)
        response.save()

    return  redirect('index')

