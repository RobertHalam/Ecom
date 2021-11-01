from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models.customer import Customer
from .models.category import Category
from .models.product import Product
from .models import customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

from .models import product



# test
# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$260000$klGCkcSwvlorrn2saMyCnE$LiixrKEPhkA2cLkeLMYscTKI3b+KEledzCFhxrE3DaA='))



# Create your views here.

class Index(View):

    def post(self,request):

        product = request.POST.get('product')

        cart=request.session.get('cart')
        if cart:
            quantity =cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        print(cart)
        request.session['cart']=cart
        return redirect('index')
        



    def get(self,request):
        products = None

        

        categories = Category.get_all_categories()
        categoryID=request.GET.get('category')
        print(categoryID)
        if categoryID:
            products = Product.get_all_product_by_category_id(categoryID)
        else:
            products = Product.get_all_product()

        data={}
        data['products'] = products
        data['categories'] = categories

        print(request.session.get('email'))

        
        return render(request,"index.html",data)

   




class Signup(View):
    def get(self,request):
        return render(request,"signup.html")



    def post(self,request):
        postData=request.POST 
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email,
        }
        error_msg=None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)

        error_msg = self.validateCustomer(customer)
            # save
        if not error_msg:
            print(first_name,last_name,phone,email,password)
            
            # hashing password
            customer.password = make_password(customer.password)
            # save
            customer.save()
            return redirect("index")

        else:
            data={
                'error' : error_msg,
                'values':value
            }
            # customer.register()
            # return HttpResponse(request.POST.get('email'))
            # return render(request,"signup.html")
        # return render(request,"signup.html",{'data':data})
        return render(request,"signup.html",data)


    def validateCustomer(self,customer):
        error_msg=None
        if (not customer.first_name):
            error_msg="First Name Required!!!"
        elif len(customer.first_name)<4:
            error_msg="First Name should be 4 char long!!!"

        if (not customer.last_name):
            error_msg="last Name Required!!!"
        elif len(customer.last_name)<4:
            error_msg="last Name should be 4 char long!!!"

        if (not customer.phone):
            error_msg="Phone Required!!!"
        elif len(customer.phone) <=9:
            error_msg="Phone should be 10 char long!!!"

        if (not customer.password):
            error_msg="Password Required!!!"
        elif len(customer.password)<3:
            error_msg="Password should be 4 char long!!!"
 
        # check email exist
        isExist = customer.isExist()
        if isExist:
            error_msg='email already exist, please try another'

        return error_msg







class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        # print(customer.email)
        # print (email,password)
        error_msg1=None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email

                return redirect("index")
            else:
                error_msg1="Email or Password Invalid"

        else:
            error_msg1="Email or Password Invalid"

        return render(request,"login.html",{'error':error_msg1
        })


        

    