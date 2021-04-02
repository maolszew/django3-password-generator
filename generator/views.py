from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html',{'password':'123456'})

def info(request):
    return render(request, 'generator/info.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'): #bo <input type="checkbox" name="uppercase">
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'): #bo <input type="checkbox" name="special">
        characters.extend(list('!@#$%^&*()/;:,.<>"*'))
    if request.GET.get('numbers'): #bo <input type="checkbox" name="numbers">
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length','12')) #bo w home.html jest <select name="length"> a 12 to default na wypadek braku parametru
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})