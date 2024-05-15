from django.shortcuts import render
from django.http import HttpResponse

def samp(request):
    return HttpResponse('<h1>hi.. hello</h1>')