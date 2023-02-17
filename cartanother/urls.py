from django.urls import path,include
# from cart import views
from cartanother import views
urlpatterns = [
    path('addtocart', views.add_to_cart),
    path('cartitemdelete/<int:id>', views.cartItemDelete),
    path('order',views.order),
    ###working on dashboard
    # path('newadminpanel', views.newadminpanel,name='dashboard'),
    # path('servicelist', views.servicelist,name='servicelist'),
    # path('alluserlist', views.alluserlist,name='userlist'),
]