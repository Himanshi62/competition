from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount

## import data tables from database
from .models import Mtt


# Create your views here.


def mtt(request):
    user = request.user
    is_filled_mtt = False 
    if user.is_authenticated:
        email = user.email
        is_filled_mtt = len(Mtt.objects.filter(email=email))==1
        
    return render(request, "mtt.html",
    {
        'is_filled_mtt':is_filled_mtt
    })
    
    
def mtt_reg(request):
    if request.method == "POST":
        
        user = request.user
        email = user.email
        name = request.POST.get('name', '')
        colg = request.POST.get('colg', '')
        email1 = request.POST.get('email1', '')
        contact = request.POST.get('contact', '')
        ref = request.POST.get('ref', '')
        year = request.POST.get('year', '')
        response = Mtt( email=email, name=name, email1=email1, colg=colg, contact=contact, year=year, ref=ref)
        response.save()

    return  redirect('mtt')
