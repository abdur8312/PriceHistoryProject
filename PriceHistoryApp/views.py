from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import users
from django.urls import reverse

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def registeruser(request):
    a = request.POST['email']
    b = request.POST['password']
    c = request.POST['name']
    d = request.POST['phone']
    user = users(email=a, password=b, name=c, phone=d)
    user.save()
    return HttpResponseRedirect(reverse('login'))
