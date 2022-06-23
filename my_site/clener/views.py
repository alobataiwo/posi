from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def simple_view(request):
    return HttpResponse(' you are welcome!')

def design(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'clener/index.html',context=x)
def login_view(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'clener/login.html',context=x)
def signup(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'clener/signup.html',context=x)


