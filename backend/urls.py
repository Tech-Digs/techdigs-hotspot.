# ###Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# ###

from django.urls import path

from backend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm/<int:package_id>/', views.confirms, name='confirm'),
    path('payment/<int:package_id>/',views.mpesa_payment, name='payment'),
    path('callback/<int:package_id>', views.callback,name='callback'), 
    path('check_payment/<str:checkout_id>/', views.check_payment_status, name='check_payment_status'),
    path('success/', views.payment_success, name='payment_success'),
    path('reconnection/<str>:voucher_code/',views.reconnection,name='reconnection')
    
]