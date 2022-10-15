from django.shortcuts import HttpResponse, render
from app1.models import breakes

# Create your views here.

def save_u(request):

    name = request.POST['username1']
    pswrd = request.POST['passs']



    print('success')
    data = breakes()
    data.user_n=name
    data.user_p=pswrd
    data.save()

    return render(request, 'app1/template4.html')
