from django.shortcuts import render,HttpResponseRedirect,redirect

import service
from .models import Sheba
from .forms import Service
from account.models import User
# Create your views here.

# def postservice(request):
#     if request.method =="POST":
#         fm= Service(request.POST)
#         if fm.is_valid():
#             usr = User.objects.get(id=request.user.id)
#             st=fm.cleaned_data['servicetitle']
#             sd=fm.cleaned_data['servicedetails']
#             sc=fm.cleaned_data['servicecategory']
#             sp=fm.cleaned_data['serviceprice']
#             sl=fm.cleaned_data['servicelocation']
#             reg = Sheba(user=usr,servicetitle=st,servicedetails=sd,servicecategory=sc,serviceprice=sp,servicelocation=sl)
#             reg.save()
#             fm = Service()
#     else:
#         fm=Service()
#     return render(request,'service/5servicepage.html',{"form":fm})


def postservice(request):
        if request.method =='POST':
                usr = User.objects.get(id=request.user.id)
                st=request.POST['servicetitle']
                sd=request.POST['servicedetails']
                sc=request.POST['servicecategory']
                sp=request.POST['serviceprice']
                sl=request.POST['servicelocation']
                reg = Sheba(user=usr,servicetitle=st,servicedetails=sd,servicecategory=sc,serviceprice=sp,servicelocation=sl)
                reg.save()
                return redirect('serviceshow')
                # fm = Service()
        else:
          fm = Service()
        return render(request,'service/5servicepage.html',{"form":fm})


def serviceshow(request):
    service = Sheba.objects.filter(user__id=request.user.id)
    return render(request,'service/myservice.html',{"service":service})

# def serviceedit(request,id):
#         service = Sheba.objects.filter(user__id=request.user.id)
#         print (service)
#         return service

def servicedelete(request,id):
        if request.method =='POST':
          pi =Sheba.objects.get(pk=id)
          pi.delete()

        return HttpResponseRedirect('/service/serviceshow/')

def serviceupdate(request,id):
        if request.method =='POST':
         pi = Sheba.objects.get(pk=id)
         fm= Service(request.POST, instance=pi)
         if fm.is_valid():
                fm.save()
                return redirect('serviceshow')
        else:
         pi = Sheba.objects.get(pk=id)
         fm= Service(instance=pi)
        #  fm.save()
            
        return render(request,'service/updateseller.html',{'form':fm})

##single page showing
def singleservice(request,id):
        value = Sheba.objects.get(pk=id)
        return render(request,'service/singleservice.html',{"value":value})