from django.urls import path
from account import views
urlpatterns = [
   path('', views.home, name='home'),
   
   # path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('sellerdashboard/',views.sellerdashboard, name='sellerdashboard'),
    path('sellerpendingorder/',views.sellerpendingorder,name='sellerpendingorder'),
    path('buyerdashboard/',views.buyerdashboard, name='buyerdashboard'),
    path('buyerorder/',views.buyerorder,name='buyerorder'),
    path('buyerorder/cancel/<id>',views.cancelorder,name='cancelorder'),
    path('buyerorder/edit',views.editorder,name='editoreder'),
    path('buyerorderrecieve/',views.buyerorderrecieve,name='buyerorderrecieve'),
    path('finalordercompleted/',views.finalordercompleted,name='finalordercompleted'),
    path('singleprofile/',views.singleprofile,name='singleprofile'),
    path('ordercompleted/',views.ordercompleted,name='ordercompleted'),
    path('sellerreview/',views.sellerreview,name='sellerreview'),
    path('reviewpost/',views.reviewpost,name='reviewpost'),
    path('buyerreview/',views.buyerreview,name='buyerreview'),
    path('buyerreviewpost/',views.buyerreviewpost,name='buyerreviewpost'),

   #  path('adminpage/', views.admin, name='adminpage'),
   #  path('customer/', views.customer, name='customer'),
   #  path('employee/', views.employee, name='employee'),
]