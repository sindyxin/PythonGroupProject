# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# username: admin
# password: python
def admin_login(request):
    # check if username in db
    try: 
        admin = Admin.objects.get(username = request.POST['username'])
    except:
        messages.error(request,'username or Password incorrect.')
        return redirect('/admin')
    # check if password correct
    if (request.POST['password'], admin.password):
        request.session['admin_id'] = admin.id
        return redirect('/admin_dashboard')
    else:
        messages.error(request,'Email or Password incorrect.')
        return redirect('/admin')

def admin_dashboard(request):
    return render(request,'eCommerce/admin_orders.html')

# Create your views here.
def admin(request):
    #show all the orders on dashboard
    return render(request,'eCommerce/admin_orders.html')

def admin_index(request):
    #login
    return render(request,'eCommerce/admin_index.html')

def admin_products(request):
    #show all the products
    return render(request,'eCommerce/admin_products.html')

def admin_orderdetail(request):
    #show info of a single order
    return render(request,'eCommerce/admin_orderdetail.html')

def admin_productdetail(request):
    #update info for a product
    return render(request,'eCommerce/admin_productdetail.html')
