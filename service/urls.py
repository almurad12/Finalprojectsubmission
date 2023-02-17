from django.urls import path,include
from service import views
urlpatterns = [
    path('postservice/',views.postservice, name='postservice'),
    path('serviceshow/', views.serviceshow,name='serviceshow'),
    # path('serviceshow/<int:id>/edit/', views.serviceedit, name='Serviceedit'),
    path('servicedelete/<int:id>/',views.servicedelete, name = 'servicedelete'),
    path('updateseller/<int:id>',views.serviceupdate, name='serviceupdate'),
    path('<int:id>',views.serviceupdate, name='serviceupdate'),

    path('singleservice/<int:id>', views.singleservice),
   
]