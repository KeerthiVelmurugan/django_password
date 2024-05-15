from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse( "hello... ")
    return render(request, 'generator/home.html')

def about(request):
    # return HttpResponse( "hello... ")
    return render(request, 'generator/about.html')

def eggs(request):
    return HttpResponse("eggs are tasty")

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length =int(request.GET.get('length',10))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword = ''
    for x in range(length):

        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
