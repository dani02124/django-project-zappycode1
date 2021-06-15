from django.shortcuts import render
import random
# Create your views here.
def generate(request):
    return render(request,'alioo/generate.html')

def password(request):

    charcters=list('abcdefghijklmnopqrstuvwxyz')

    lenght=int(request.GET.get('lenght'))

    if request.GET.get('numbers'):
        charcters.extend('1234567890')
    if request.GET.get('special'):
        charcters.extend('!@#$%^&*')
    if request.GET.get('uppercase'):
        charcters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    thepas=''
    for x in range(lenght):
        thepas += random.choice(charcters)

    return render(request,'alioo/password.html',{'password':thepas})
def about(request):
    return render(request,'alioo/about.html')
