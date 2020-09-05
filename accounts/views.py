from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    context = {
        'orders': orders, 
        'customers':customers,
        'total_orders':total_orders,
        'total_customers':total_customers,
        'delivered':delivered,
        'pending':pending
        }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'accounts/products.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')
