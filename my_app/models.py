from django.db import models

# Create your models here.

class tb_login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    user_type=models.CharField(max_length=30)
    
    
    
class tb_registration(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    pincode=models.CharField(max_length=10)
    housename=models.CharField(max_length=30)
    place=models.CharField(max_length=20)
    landmark=models.CharField(max_length=40)
    login=models.ForeignKey('tb_login',on_delete=models.CASCADE)
    
    
    
class tb_shop_registrations(models.Model):
    login=models.ForeignKey('tb_login',on_delete=models.CASCADE)
    shopname=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    landmark=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    status=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    

class tb_product_category(models.Model):
    category_name=models.CharField(max_length=100)
    
    
class tb_vendors(models.Model):
    company_name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    est_year=models.CharField(max_length=100)
    
    
class tb_product(models.Model):
    product_name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    price=models.CharField(max_length=20)
    image=models.CharField(max_length=20)   
    category=models.ForeignKey('tb_product_category',on_delete=models.CASCADE)
    shop_registrations=models.ForeignKey('tb_shop_registrations',on_delete=models.CASCADE)
    stocks=models.CharField(max_length=20)
    
    
class tb_stocks(models.Model):
    quantity=models.CharField(max_length=20)
    date_time=models.CharField(max_length=20)
    product=models.ForeignKey('tb_product',on_delete=models.CASCADE)
    
    
    
class tb_complaints(models.Model):
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=100)
    date_time=models.CharField(max_length=20)
    user=models.ForeignKey('tb_registration',on_delete=models.CASCADE)
    
    
class tb_order_master(models.Model):
    date_time=models.CharField(max_length=20)
    total=models.CharField(max_length=100)
    status=models.CharField(max_length=20)
    shop_registrations=models.ForeignKey('tb_shop_registrations',on_delete=models.CASCADE)
    user=models.ForeignKey('tb_registration',on_delete=models.CASCADE)
    
    
class tb_order_details(models.Model):
     product=models.ForeignKey('tb_product',on_delete=models.CASCADE)
     quantity=models.CharField(max_length=20)
     amount=models.CharField(max_length=20)
     order_master=models.ForeignKey('tb_order_master',on_delete=models.CASCADE)
     
     
class tb_rating(models.Model):
    rate=models.CharField(max_length=20)
    review=models.CharField(max_length=200)
    date_time=models.CharField(max_length=20)
    product=models.ForeignKey('tb_product',on_delete=models.CASCADE)
    user=models.ForeignKey('tb_registration',on_delete=models.CASCADE)   
    
    
class tb_payment(models.Model):
    date=models.CharField(max_length=100)
    amount=models.CharField(max_length=20)
    order_master=models.ForeignKey('tb_order_master',on_delete=models.CASCADE)  