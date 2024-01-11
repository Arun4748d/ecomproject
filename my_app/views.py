from django.shortcuts import render,HttpResponse
from my_app.models import *
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        user=request.POST['user_name']
        password=request.POST['password']
        f=tb_login.objects.get(username=user,password=password)
        if f:
            request.session['login_id']=f.pk
            if f.user_type == 'admin':
                return HttpResponse("<script>alert('successfully');window.location='/admin_home'</script>")
            if f.user_type=='user':
                return HttpResponse("<script>alert('successfully');window.location='/user_home'</script>")
            if f.user_type =='shop':
                return HttpResponse("<script>alert('successfully');window.location='/shop'</script>")
            
    return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        phoneno=request.POST['phone_no']
        pincode=request.POST['pin_code']
        housename=request.POST['house_name']
        place=request.POST['place_']
        landmark=request.POST['land_mark']
        
        user=request.POST['user_name']
        password=request.POST['password']
        f=tb_login(username=user,password=password,user_type='user')
        f.save()
        c=tb_registration(firstname=firstname,lastname=lastname,email=email,phone=phoneno,pincode=pincode,housename=housename,place=place,landmark=landmark,login=f)
        c.save()
        return HttpResponse("<script>alert('successfully');window.location='login'</script>")
        
    return render(request,'registration.html')


def admin_home(request):
    return render(request,'admin_home.html')


def user_home(request):
    if request.method=='POST':
        product=request.POST['product_name']
        view=tb_product.objects.filter(product_name=product) | tb_product.objects.filter(price=product)
    else:
        view=tb_product.objects.all() 
    return render(request,'user_home.html',{'view':view})

def shop_registration(request):
    if request.method=='POST':
        shopname=request.POST['shop_name']
        place=request.POST['pla_ce']
        landmark=request.POST['landmark']
        phone=request.POST['phone_']
        email=request.POST['email']
        user=request.POST['user_name']
        password=request.POST['password']
        f=tb_login(username=user,password=password,user_type='pending')
        f.save()
        g=tb_shop_registrations(shopname=shopname,place=place,landmark=landmark,phone=phone,email=email,username=user,status='pending',password=password,login=f)
        g.save()
        return HttpResponse("<script>alert('successfully');window.location='login'</script>")
    
    return render(request,'shop_registration.html')
    
    
    
def view_shop_admin(request):
    s=tb_shop_registrations.objects.all()
    print(s)
    return render(request,'view_shop_admin.html',{'q':s})



def accept_usertype(request,login_id):
    qr=tb_login.objects.get(id=login_id)
    a=tb_shop_registrations.objects.get(login_id=login_id)
    a.status='shop'
    a.save()
    qr.user_type='shop'
    qr.save()
    return HttpResponse("<script>alert('accepted');window.location='/admin_home'</script>")

def reject_usertype(request,id):
    s=tb_shop_registrations.objects.filter(id=id)
    s.delete()
    return HttpResponse("<script>alert('successfully');window.location='/admin_home'</script>")
    return render(request,'view_shop_admin.html')


def shop(request):
    return render(request,'shop.html')

def admin_productcategory(request):
    f=tb_product_category.objects.all()
    if request.method=='POST':
        category=request.POST['category']
        c=tb_product_category(category_name=category)
        c.save()
    
    return render(request,'admin_productcategory.html',{'h':f})


def view_customer(request):
    s=tb_registration.objects.all()
    
    return render(request,'view_customer.html',{'f':s})

def delete_c(request,id):
    a=tb_registration.objects.get(id=id)
    a.delete()
    return HttpResponse("<script>alert('successfully');window.location='/view_customer'</script>")
    return render(request,'view_customer.html')


def send_complaints(request):
    
    today=date.today()
    qr=tb_complaints.objects.all()
    
    
    lid=request.session['login_id']
    uid=tb_registration.objects.filter(login_id=lid)
    if uid:
        uids=uid[0].id
    
    if request.method=='POST':
        complaints=request.POST['complaints']
        f=tb_complaints(complaint=complaints,date_time=today,reply='pending',user_id=uids)
        f.save()
        qr.save()
        
    
    return render(request,'send_complaints.html',{'n':qr})


def viewcomplaints(request):
    s=tb_complaints.objects.all()
    
    return render(request,'viewcomplaints.html',{'g':s})


    

def replycomplaint(request,id):
    
    s=tb_complaints.objects.get(id=id)
    if request.method=='POST':
       s.reply=request.POST['reply']
       s.save()
       
    
    return render(request,'replycomplaint.html')


def delete_c(request,id):
    s=tb_registration.objects.get(id=id)
    s.delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_customer'</script>")
    return render(request,'admin_productcategory.html')
    


def update_c(request,id):
    s=tb_product_category.objects.get(id=id)
    if request.method=='POST':
        s.category_name=request.POST['category']
        s.save()
        return HttpResponse("<script>alert('updated');window.location='/admin_productcategory'</script>")
    return render(request,'admin_productcategory.html',{'f':s})
    
    
def view_productcategoryshop(request):
    g=tb_product.objects.all()
    lid=request.session['login_id']
    
    f=tb_product_category.objects.all()
  
    # s=tb_product_category.objects.get(id=id)
    # if s:
    #     procat:s[0].id
    d=tb_shop_registrations.objects.filter(login_id=lid)
    if d:
        shopreg=d[0].id
    if request.method=='POST':
        productname=request.POST['proname']
        details=request.POST['details']
        price=request.POST['price']
        c=request.POST['catename']
        i=request.FILES['imagexxx']
        fss=FileSystemStorage()
        k=fss.save(i.name,i)
        stock=request.POST['quantity']
        q=tb_product(product_name=productname,details=details,price=price,image=k,category_id=c,shop_registrations_id=shopreg,stocks=stock)
        q.save()
   
        
    
    return render(request,'view_productcategoryshop.html',{'catview':f,'man':g})





def delete_cat(request,id):
    f=tb_product.objects.get(id=id)
    f.delete()
    return render(request,'view_productcategoryshop.html')



def update_cat(request,id):
    g=tb_product_category.objects.all()
    f=tb_product.objects.get(id=id)
    if request.method=='POST':
        f.product_name=request.POST['proname']
        f.details=request.POST['details']
        f.price=request.POST['price']
        i=request.FILES['imagexxx']
        fss=FileSystemStorage()
        k=fss.save(i.name,i)
        f.image=k
        f.category_id=request.POST['catename']
        f.stocks=request.POST['quantity']
        f.save()
        return HttpResponse("<script>alert('updated');window.location='/view_productcategoryshop'</script>")
    return render(request,'view_productcategoryshop.html',{'j':f ,'catview':g})



def viewproductsadmin(request):
    d=tb_product.objects.all()
    return render(request,'viewproductsadmin.html',{'f':d})


def add_to_cart(request,id,price,shop_registrations_id):
    
    pid=id
    lid=request.session['login_id']
    q1=tb_registration.objects.filter(login_id=lid)
    if q1:
        uid=q1[0].id
        
    # lid=request.session['login_id']
    # q2=tb_shop_registrations.objects.filter(login_id=lid)
    # if q2:
    #     sid=q2[0].id
    today=date.today()
        
    q=tb_product.objects.get(id=id)
    if request.method=='POST':
        productname=request.POST['proname']
        price=request.POST['price']
        quantity=request.POST['quantity']
        total=request.POST['total']
        print(productname,price,quantity,total)
        
        q=tb_order_master.objects.filter(status='pending',user_id=uid)
        if q:
            tot=q[0].total
            print('ffff',tot)
            oid=q[0].id
            
        
            try:     
                wers=tb_order_details.objects.get(order_master_id=oid,product_id=pid,)
                oiqty=wers.quantity
                amt=wers.amount
                omid=wers.order_master_id
                qu=oiqty+int(quantity)
                wers.quantity=qu
                am=amt+int(price)
                wers.amount=am
                wers.save()
                r=tb_order_master.objects.get(id=omid)
                if r:
                    r.total=wers.quantity * wers.amount
                    r.save()
            except:
                  q=tb_order_master.objects.get(id=oid)
                  if q:
                    totals=int(tot)+int(total)
                    q.total=totals
                    q.save()
                    b=tb_order_details(amount=price,quantity=quantity,product_id=pid,order_master_id=oid)
                    b.save()
        else:
            a=tb_order_master(total=total,status="pending",date_time=today,user_id=uid,shop_registrations_id=shop_registrations_id)
            a.save()
            c=tb_order_details(quantity=quantity,amount=price,order_master_id=a.pk,product_id=pid)
            c.save()
      
    return render(request,'add_to_cart.html',{'q':q,'amount':price})

        





def view_cart(request):
    b=tb_order_details.objects.all()
    c=tb_order_master.objects.all()
    
    
    
    return render(request,'view_cart.html',{'c':b,'d':c})





def payment(request,id,total):
    oid=id
   
  
    if request.method=='POST':
        date_n=request.POST['exp_date']
        amount_n=request.POST['amount']
        q=tb_payment(date=date_n,amount=amount_n,order_master_id=oid)
        q.save()
        a=tb_order_master.objects.get(id=id)
        a.status='paid'
        a.save()
        return HttpResponse("<script>alert('successfully');window.location='view_cart'</script>")
    return render(request,'payment.html',{'total':total})


def rate_product(request,id,product_id):
    
    lid=request.session['login_id']
    q1=tb_registration.objects.filter(login_id=lid)
    if q1:
        uid=q1[0].id
    # q=tb_product.objects.get(id=id)
    today=date.today()
    if request.method=='POST':
        rates=request.POST['rating']
        rev=request.POST['review']
        q=tb_rating(rate=rates,date_time=today,review=rev,user_id=uid,product_id=product_id)
        
        q.save()
    
    return render(request,'rate_product.html')


def view_rating(request):
    g=tb_rating.objects.all()
    return render(request,'view_rating.html',{'f':g})


def view_order(request):
    f=tb_order_details.objects.all()
    return render(request,'view_order.html',{'j':f})

def accept_p(request,id):
    a=tb_order_master.objects.get(id=id)
    a.status = 'delivered'
    a.save()
    return HttpResponse("<script>alert('successfully');window.location='view_order'</script>")
    # return render(request,'view_order.html')
    
    
    
def search_results(request):
    f=tb_product.objects.all()
    return render(request,'search_results.html',{'n':f})


def android_login(request):
    data = []
    andusername=request.GET.get('username')
    andpassword=request.GET.get('password')
    
    try:
        queryset = tb_login.objects.filter(username=andusername, password=andpassword)
        for q in queryset:
            data.append({
                'id': q.id,
                'username': q.username,
                'password': q.password,
                'user_type':q.user_type
                # Add other fields you want to include in the response
            })
        if data:
            status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tb_login.DoesNotExist:
        status = "error"
        message = "Invalid credentials"

    response = {
        'status': status,
        'data': data
    }
    print(data)
    return JsonResponse(response)
    



def android_registration(request):
    data = []
    andfirstname=request.GET.get('firstname')
    andlastname=request.GET.get('lastname')
    andemail=request.GET.get('andemail')
    andphone_no=request.GET.get('phone_no')
    andhouse_name=request.GET.get('house_name')
    andpincode=request.GET.get('pincode')
    andplace=request.GET.get('place')
    andlandmark=request.GET.get('landmark')
    usernamess=request.GET.get('usernamess')
    andpassword=request.GET.get('password')
    try:
        querylog = tb_login(username=usernamess, password=andpassword,user_type='user')
        querylog.save()
        queryuse= tb_registration(firstname= andfirstname,lastname= andlastname,phone= andphone_no,email= andemail,housename= andhouse_name,pincode= andpincode,place=andplace,landmark=andlandmark,login=querylog)
        queryuse.save()
        if data:
                status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tb_login.DoesNotExist:
        status = "error"
        message = "Invalid credentials"
    response = {
        'status': status,
        'data': data
    }

    if status == "error":
        response['message'] = message

    return JsonResponse(response)
    



 
def userviewshop(request):
    data = {}
    try:
        shopview=tb_shop_registrations.objects.all()
        data['status'] = 'success'
        data['data'] = []
        for shop in shopview:
            shop_data ={
                'shopname':shop.shopname,
                'place':shop.place,
                'landmark':shop.landmark,
                'email':shop.email,
            }
            data['data'].append(shop_data)
    except tb_shop_registrations.DoesNotExist:
        data['status'] = 'failed'
    data['method'] = 'viewshop'
    return JsonResponse(data)


def userview(request):
    data ={}
    try:
        user=tb_registration.objects.all()
        data['status'] = 'success'
        data['data'] = []
        for users in user:
            user_data ={
                'firstname':users.firstname,
                'place':users.place,
                'phone':users.phone,
                'email':users.email,
            }
            data['data'].append(user_data)
    except tb_registration.DoesNotExist:
        data['status'] = 'failed'
    data['method'] = 'viewuser'
    return JsonResponse(data)

 
def send_complaintss(request):
    data = []
    today=date.today()
    andsend=request.GET.get('complaint')
    lid=request.GET.get('lid')
    
    try:
        query=tb_complaints(complaint=andsend,user_id=lid,reply='pending',date_time=today)
        query.save()
        if data:
                status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tb_complaints.DoesNotExist:
        status = "error"
        message = "Invalid credentials"
    response = {
        'status': status,
        'data': data
    }

    if status == "error":
        response['message'] = message

        return JsonResponse(response)
    
    
    
def  view_complaints(request):
    data ={}
    try:
        user=tb_complaints.objects.all()
        data['status'] = 'success'
        data['data'] = []
        for comp in user:
            view_data ={
                'complaint':comp.complaint,
                'reply':comp.reply,
                'date_time':comp.date_time,
                
            }
            data['data'].append(view_data)
    except tb_complaints.DoesNotExist:
        data['status'] = 'failed'
    data['method'] = 'viewcomp'
    return JsonResponse(data)





def send_reply(request,id):
    data=[]
    
    f=request.GET.get(id=id)
    
    
    try:
        f.reply=request.get['reply']
        f.save()
        if data:
                status = "success"
        else:
            status = "error"
            message = "Invalid credentials"
    except tb_complaints.DoesNotExist:
        status = "error"
        message = "Invalid credentials"
    response = {
        'status': status,
        'data': data
    }

    if status == "error":
        response['message'] = message

        return JsonResponse(response)
    
    


    
  

    
    



        

            
          







    

    