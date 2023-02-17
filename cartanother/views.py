from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,redirect
from account.models import User
from service.models import Sheba
from cart.models import Cart
from cartanother.models import Cartanother,Order,Ordernew,Cartanothernew
from django.http import JsonResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from pysslcmz.payment import SSLCSession

from decimal import Decimal


def add_to_cart(request):
    if request.method =='GET':
        # usr = User.objects.get(id=request.user.id)
        service_id =Sheba.objects.get(id=request.GET['serviceid'])
        user_id =User.objects.get(id=request.GET['userid'])
        ###another way
        servicetitle = request.GET.get('servicetitle') 
        serviceprice = request.GET.get('serviceprice')
        serviceuseridnum = request.GET.get('serviceuseridnum')
        # service_title = Sheba.objects.get(servicetitle=request.GET['servicetitle'])
        # service_price = Sheba.objects.get(serviceprice=request.GET['serviceprice'])
        print(serviceprice,servicetitle)
        ##trying something
        is_exist =Cartanothernew.objects.filter(user=user_id,service=service_id)
        print(len(is_exist))
        if len(is_exist)>0:
            msg ="data already exist"
        else:
        # cart = Cart(user=user_id,service=service_id)
        # cart = Cartanother(user=user_id,service=service_id,servicetitle=servicetitle,serviceprice=serviceprice)
            cart = Cartanothernew(user=user_id,service=service_id,servicetitle=servicetitle,serviceprice=serviceprice,serviceuseridnum=serviceuseridnum)
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

def cartItemDelete(request,id):
    if request.method =='GET':
        # data_id =  Cartanother.objects.get(id=id) 
        data_id =  Cartanothernew.objects.get(id=id)
        data_id.delete()
        print(data_id)
    return redirect('buyerdashboard')

def order(request):
    if request.method =="POST":
        cartid = request.POST['cartid']
        serviceuserid=request.POST['serviceuserid']
        userid = request.POST['userid']
        serviceid = request.POST['serviceid']
        servicetitle = request.POST['servicetitle']
        serviceprice = request.POST['serviceprice']
        date = request.POST['date']
        time = request.POST['time']
        address = request.POST['address']
        phoneno = request.POST['phoneno']


        # order = Order(cartid=cartid,userid=userid,serviceid=serviceid,orderservicetitle=servicetitle,orderserviceprice=serviceprice,orderdate=date,orderaddress=address,orderphoneno=phoneno)
        # order.save()
        ##for payment
        mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='nothi63cf7bddea746', sslc_store_pass='nothi63cf7bddea746@ssl')
        mypayment.set_urls(success_url='http://127.0.0.1:8000/payment/success', fail_url='http://127.0.0.1:8000/payment/failed', cancel_url='http://127.0.0.1:8000/payment/cancel', ipn_url='https://www.try.com/ipn_listener/')
        mypayment.set_product_integration(total_amount=serviceprice, currency='BDT', product_category='service', product_name='servicetitle', num_of_item=1, shipping_method='YES', product_profile='None')
        mypayment.set_customer_info(name='user', email='user@email.com', address1=address, address2='none', city='Dhaka', postcode='1207', country='Bangladesh', phone=phoneno)
        mypayment.set_shipping_info(shipping_to=address, address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
        response_data = mypayment.init_payment()
        print("response data is",response_data['status'])
        print("response data is",response_data)

        if response_data['status']=="SUCCESS":
        # if success_url=="True"
        # if response_data['status']=="no":
            # response_data = mypayment.init_payment()
            ordernew = Ordernew(cartid=cartid,userid=userid,serviceuserid=serviceuserid,serviceid=serviceid,orderservicetitle=servicetitle,orderserviceprice=serviceprice,orderdate=date,time=time,orderaddress=address,orderphoneno=phoneno)
            ordernew.save()
            cartdelete =Cartanothernew.objects.get(id=cartid)
            cartdelete.delete()
            print(cartid,userid,serviceid,servicetitle,serviceprice,date,address,phoneno)
            return redirect(response_data['GatewayPageURL'])
        else:
            # return redirect()
            return redirect('http://127.0.0.1:8000/account/buyerdashboard/')
            # print("Order is failed")

    # return redirect('buyerdashboard')
