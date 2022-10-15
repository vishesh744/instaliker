from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def likes(request):
    return render(request, 'login.html')
