from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from pysslcmz.payment import SSLCSession

from decimal import Decimal

# mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='your_sslc_store_id', sslc_store_pass='your_sslc_store_passcode')
@csrf_exempt
def success(request):
    return render(request,'payment/success.html')
@csrf_exempt
def failed(request):
    return render(request,'payment/failed.html')
@csrf_exempt
def cancel(request):
    return render(request,'payment/cancel.html')

@csrf_exempt
def payment(request):
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='nothi63cf7bddea746', sslc_store_pass='nothi63cf7bddea746@ssl')
    
    mypayment.set_urls(success_url='http://127.0.0.1:8000/payment/success', fail_url='http://127.0.0.1:8000/payment/failed', cancel_url='http://127.0.0.1:8000/payment/cancel', ipn_url='https://www.try.com/ipn_listener/')
    mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', product_name='demo-product', num_of_item=2, shipping_method='YES', product_profile='None')
    mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')
    mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
    response_data = mypayment.init_payment()
    print(response_data['status'])
    a = response_data['status']
    b ='SUCCESS'
    c='FAILED'
    if a==b:
        print('order created')
    else:
        print('order is failed')
    return redirect(response_data['GatewayPageURL'])
    
        
    # if response_data['status']== "SUCCESS":
    #     print("Order created successfully")
    # else:
    #     print("ordered failed ")

    # return render(request,'payment/payment.html'),