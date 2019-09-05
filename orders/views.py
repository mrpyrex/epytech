from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from address.models import Address
from cart.views import _cart_id
from cart.models import CartItem, Cart
from .models import Order, OrderItem

# Create your views here.


def order_create(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    address = Address.objects.get(
        customer=request.user, address_type='billing')
    customer = request.user
    billing_address1 = address.billing_address1
    billing_address2 = address.billing_address2
    phone = address.phone
    country = address.country
    state = address.state
    city = address.city
    post_code = address.post_code

    try:
        order = Order.objects.create(billing_address1=billing_address1, customer=customer, billing_address2=billing_address2,
                                     phone=phone, country=country, state=state, city=city, post_code=post_code)
        order.save()

        for order_item in cart_items:
            oi = OrderItem.objects.create(
                product=order_item.product,
                price=order_item.product.price,
                quantity=order_item.quantity,
                order=order
            )
            oi.save()
        request.session['order_id'] = order.id
        # return redirect(reverse('payment:process'))
    except ObjectDoesNotExist:
        pass

    return render(request, 'orders/create.html', {'cart': cart})
