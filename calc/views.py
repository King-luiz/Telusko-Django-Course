from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Jane'})

def about(request):
    return render(request, 'about.html')

def blue(request):
    return render(request, 'blue.html')

def block(request):
    return render(request, 'blue.html')

def result(request):
    return render(request, 'result.html')
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
