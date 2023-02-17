from django.urls import path,include
from payment import views
urlpatterns = [
    path('success', views.success),
    path('failed', views.failed),
    path('cancel', views.cancel),
    path('payment',views.payment,name="payment"),

]