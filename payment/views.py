from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from django.contrib.auth.models import User
from shop.models import Product


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    paystack_total = int(order.get_total_cost() * 100)
    data_key = settings.PAYSTACK_PUBLIC_KEY
    data_email = request.user.email

    # products = Product.objects.get(id=order_item.product.id)
    # products.stock = int(order_item.product.stock - order_item.quantity)
    # products.save()
    # order_item.delete()
    context = {
        'order': order,
        'paystack_total': paystack_total,
        'data_key': data_key,
        'data_email': data_email
    }
    return render(request, 'payment/process.html', context)
