from django.shortcuts import HttpResponse, render
from app1.models import breakes
import random
from app1.models import breakes

# Create your views here.

def save_u(request):
    from app1.models import breakes
    if request.method=='POST':

        
        random_page=random.randint(0, 2)
        page = ['template3.html', 'template4.html', 'template5.html']
        display_page=page[random_page]

        name = request.POST.get('username1')
        pswrd = request.POST['passs']
        # mydata = breakes.objects.all()
        # bres = breakes.objects.all()
        # print('success')
        data = breakes()
        data.user_n=name
        data.user_p=pswrd
        data.save()
        return render(request, f"app1/{display_page}")
    else:

        return HttpResponse('something is wrong')
