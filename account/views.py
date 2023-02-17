from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from .models import User
from account import views
# from cart.models import Cart
from cartanother.models import Cartanother
## call service model
from service.models import Sheba
from  cartanother.models import Cartanother
from  cartanother.models import Cartanothernew
from django.db.models import Count
from account.models import User
from django.db.models import Q
from cartanother.models import Order
from cartanother.models import Ordernew
from django.views.decorators.csrf import csrf_exempt
from account.models import Review
# Create your views here.
# from .urls import views


# def home(request):
#     return render(request,'buyinguserpage1.html')
def home(request):
    category = request.GET.get('category')
    minimum = request.GET.get('minimum')
    maximum = request.GET.get('maximum')
    print(category)
    print(minimum)
    print(maximum)
    context={}
    if minimum and maximum:
        context["servicedataset"]= Sheba.objects.filter(serviceprice__range=(minimum, maximum))
        context['feature']=Sheba.objects.filter(featureservice=True)
        context['minimumvalue']=minimum
        context['maximumvalue']=maximum

    elif category:
        context["servicedataset"] = Sheba.objects.filter(servicecategory=category)
        context['feature']=Sheba.objects.filter(featureservice=True)
    else:
        context["servicedataset"] = Sheba.objects.all()
        context['feature']=Sheba.objects.filter(featureservice=True)
    # return render(request,'slider.html',context)
    return render(request,'slider3.html',context)
    # return render(request,'Home.html',context)

###seller dashboard page
def sellerdashboard(request):
    return render(request,'4sellerdashboard.html')

###seller pending order page
def sellerpendingorder(request):
    context={}
    context['sellerpendingorder']=Ordernew.objects.filter(serviceuserid=request.user.id)
    return render(request,'service/sellerpendingorder.html',context)

@csrf_exempt
def buyerdashboard(request):
    context={}
    category =request.GET.get('category')
    minimum = request.GET.get('minimum')
    maximum = request.GET.get('maximum')

    if minimum and maximum:
        context["servicedataset"]= Sheba.objects.filter(serviceprice__range=(minimum, maximum))
        context['minimumvalue']=minimum
        context['maximumvalue']=maximum
        ###old
        carts = Cartanothernew.objects.filter(user_id = request.user.id)
        context['cartcount']= len(carts)
        context['cartvalue']=carts
        # context['addtocart']=Cartanother.objects.all()
        context['addtocart']=Cartanothernew.objects.all()
        ##for feature service
        context['feature']=Sheba.objects.filter(featureservice=True)

    elif category:
        context["servicedataset"] = Sheba.objects.filter(servicecategory=category)
        carts = Cartanothernew.objects.filter(user_id = request.user.id)
        context['cartcount']= len(carts)
        context['cartvalue']=carts
        # context['addtocart']=Cartanother.objects.all()
        context['addtocart']=Cartanothernew.objects.all()
        ##for feature service
        context['feature']=Sheba.objects.filter(featureservice=True)
        
    else:
        context["servicedataset"] = Sheba.objects.all()
        carts = Cartanothernew.objects.filter(user_id = request.user.id)
        context['cartcount']= len(carts)
        context['cartvalue']=carts
        # context['addtocart']=Cartanother.objects.all()
        context['addtocart']=Cartanothernew.objects.all()
        #for featureservice
        context['feature']=Sheba.objects.filter(featureservice=True)

    # data = Cart.objects.filter(user_id = request.user.id).select_related('service')
    # print(data[0].service)
    # return JsonResponse(list(data.values()),safe=False)
    # for cart in carts:
    #     context['cartcount'] += 1
    # print( context["cartcount"])
    # context["cartcount"]= Cart.objects.get()
    # return render(request,'7BuyerServicepage.html',context)

    # return render(request,'slider2.html',context)
    return render(request,'slider4.html',context)

# def login_view(request):
#     return render(request,'login.html')






# Create your views here.


# def index(request):
#     return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')

        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('buyerdashboard')
            elif user is not None and user.is_seller:
                login(request, user)
                return redirect('sellerdashboard')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

###logout view
def logout_view(request):
    logout(request)
    return redirect('home')

def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def buyerorder(request):
    context={}
    context['createdorder'] = Ordernew.objects.filter(userid = request.user.id)
    return render(request,'buyerorderpage.html',context)
##buyerorder recieve
def buyerorderrecieve(request):
    id = request.GET.get('id')
    orderupdate= Ordernew.objects.filter(id=id)
    orderupdate.update(order_complete=False)
    # context={}
    # context['createdorder'] = Ordernew.objects.filter(userid = request.user.id)
    return redirect('/account/buyerorder/')

def cancelorder(request,id):
    # return render (request,'buyerorderpage.html')
    deleteorder = Ordernew.objects.filter(id = id)
    deleteorder.delete()
    # return redirect('/account/buyerorder/')
    # return redirect('/account/sellerpendingorder/')
    return redirect('/account/buyerorder/')
    

def editorder(request):
    id = request.GET.get('id')
    print(id)
    editorder = Ordernew.objects.filter(id = id)
    editorder.update(accept_or_rejected=True)
    # print(editorder['cartid'])
    # user=user_id,service=service_id
    # editorder =Ordernew(id=id,accept_or_rejected=1)
    # editorder.save()
    return redirect('/account/sellerpendingorder/')


def singleprofile(request):
    if request.method == "GET":
        context={}
        id = request.GET.get('userid')

        context['user'] =User.objects.filter(id=id)
        context['review'] = Review.objects.filter(reviewreceiveid=id)
        
        a = context['review']
        b= context['review'].count()
        # print(a)
        # print(b)
        if b==0:
            context['count']=0
            context['rating']=0
        else:
            total_rating_count =0
            for data in a:
                total_rating_count =total_rating_count+data.rating 
                print(data.rating)
                print(total_rating_count)
                # print(ratingcount)
            total_review_count =  Review.objects.filter(reviewreceiveid=id).count()
            print(total_review_count)
            context['count'] = total_review_count
            # if context['count']==0:
            #    context['rating']=0
            # else:
            rating = total_rating_count/total_review_count
            context['rating']=rating
            print(rating)
            print(id)
        return render(request,'profile.html',context)

def sellerreview(request):
    if request.method=="GET":
        context={}
        context['selleruserid']= request.GET.get('reviewgivenid')
        context['buyeruserid']= request.GET.get('reviewreciveid')
        context['id']= request.GET.get('id')
        # selleruserid= request.GET.get('reviewgivenid')
        # buyeruserid= request.GET.get('reviewreciveid')
        # print(selleruserid,buyeruserid)

        return render (request,'reviewpage.html',context)

##sellerReview
def reviewpost(request):
    if request.method =="GET":
        reviewgivenid = request.GET.get('reviewgivenid')
        reviewreciveid = request.GET.get('reviewreciveid')
        star = request.GET.get('star')
        comment = request.GET.get('comment')
        id = request.GET.get('id')
        sellerReview = Review(reviewgivenid=reviewgivenid,reviewreceiveid=reviewreciveid,rating=star,comment=comment)
        sellerReview.save()
        ##review complete
        sellerreviewcomplete= Ordernew.objects.filter(id=id)
        sellerreviewcomplete.update(seller_review_complete=True)
        print(reviewgivenid, reviewreciveid,star,comment)
    return render(request,'review/ReviewThankyoupage.html')


def ordercompleted(request):
     if request.method =="GET":
        id = request.GET.get('id')
        editorder = Ordernew.objects.filter(id = id)
        editorder.update(order_complete=True)
        return redirect('/account/sellerpendingorder/')

def finalordercompleted(request):
    if request.method =="GET":
        id = request.GET.get('id')
        editorder = Ordernew.objects.filter(id = id)
        editorder.update(order_final_complete=True)
        return redirect('/account/buyerorder/')
    

def buyerreview(request):
    if request.method=="GET":
        context={}
        context['selleruserid']= request.GET.get('reviewgivenid')
        context['buyeruserid']= request.GET.get('reviewreciveid')
        context['id']= request.GET.get('id')
        # selleruserid= request.GET.get('reviewgivenid')
        # buyeruserid= request.GET.get('reviewreciveid')
        # print(selleruserid,buyeruserid)
    return render (request,'buyerreview/reviewpage.html',context)

def buyerreviewpost(request):
    if request.method =="GET":
        reviewgivenid = request.GET.get('reviewgivenid')
        reviewreciveid = request.GET.get('reviewreciveid')
        star = request.GET.get('star')
        comment = request.GET.get('comment')
        id = request.GET.get('id')
        buyerReview = Review(reviewgivenid=reviewgivenid,reviewreceiveid=reviewreciveid,rating=star,comment=comment)
        buyerReview.save()
        ##review complete
        buyerreviewcomplete= Ordernew.objects.filter(id=id)
        buyerreviewcomplete.update(buyer_review_complete=True)

        print(reviewgivenid, reviewreciveid,star,comment)
    return render(request,'buyerreview/ReviewThankyoupage.html')