"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('registration',views.registration),
    path('admin_home',views.admin_home),
    path('user_home',views.user_home),
    path('shop_registration',views.shop_registration),
    path('view_shop_admin',views.view_shop_admin),
    path('accept_usertype/<login_id>',views.accept_usertype),
    path('reject_usertype/<id>',views.reject_usertype),
    path('shop',views.shop),
    path('admin_productcategory',views.admin_productcategory),
    path('view_customer',views.view_customer),
    path('delete_c/<id>',views.delete_c),
    path('send_complaints',views.send_complaints),
    path('viewcomplaints',views.viewcomplaints),
    path('replycomplaint/<id>',views.replycomplaint),
    path('delete_c/<id>',views.delete_c),
    path('update_c/<id>',views.update_c),
    path('view_productcategoryshop',views.view_productcategoryshop),
    path('delete_cat/<id>',views.delete_cat),
    path('update_cat/<id>',views.update_cat),

   
    path('viewproductsadmin',views.viewproductsadmin),
    path('add_to_cart/<id>/<price>/<shop_registrations_id>',views.add_to_cart),
    path('view_cart',views.view_cart),
   
    path('payment/<id>/<total>',views.payment),
    path('rate_product/<id>/<product_id>',views.rate_product), 
    path('view_rating',views.view_rating),
    path('view_order',views.view_order),
    path('accept_p/<id>',views.accept_p),
  
   
    
    path('search_results/<id>',views.search_results),
    path('views/android_login',views.android_login,name='android_login'),
    path('views/android_registration',views.android_registration, name='android_registration'),
    path('views/userviewshop',views.userviewshop, name='userviewshop'),
    path('views/userview',views.userview, name='userview'),
    path('views/send_complaintss',views.send_complaintss, name='send_complaintss'),
    path('views/view_complaints',views.view_complaints, name='view_complaints'),
    path('views/send_reply',views.send_reply, name='send_reply'),
    
      
      
    
    
   
    
    

]
