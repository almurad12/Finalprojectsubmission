from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,redirect
from account.models import User
from service.models import Sheba
from cart.models import Cart
from django.http import JsonResponse
# Create your views here.


def add_to_cart(request):
    if request.method =='GET':
        # usr = User.objects.get(id=request.user.id)
        service_id =Sheba.objects.get(id=request.GET['serviceid'])
        user_id =User.objects.get(id=request.GET['userid'])
        ###another way
        servicetitle = request.GET.get('servicetitle') 
        serviceprice = request.GET.get('serviceprice')
        # service_title = Sheba.objects.get(servicetitle=request.GET['servicetitle'])
        # service_price = Sheba.objects.get(serviceprice=request.GET['serviceprice'])
        print(serviceprice,servicetitle)

        cart = Cart(user=user_id,service=service_id)
        # cart = Cart(user=user_id,service=service_id,servicetitle=servicetitle,serviceprice=serviceprice)
        cart.save()
        # return redirect('serviceshow')
        return redirect('buyerdashboard')
        # return JsonResponse({'usr': user_id,'service':service_id})
        # fm = Service()
    # else:
    #     fm = Service()
    # return render(request,'service/5servicepage.html',{"form":fm})

#new admin panel
# def newadminpanel(request):
#     return render(request,'adminpanel/cartDashboard.html')

# def servicelist(request):
#     return render(request,'adminpanel/allservicelist.html')

# def alluserlist(request):
#     return render(request,'adminpanel/alluserlist.html')
