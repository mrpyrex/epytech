# from django.shortcuts import render, redirect
# from datetime import timezone
# from django.views.decorators.http import require_POST
# from django.core.exceptions import ObjectDoesNotExist
# from .forms import CouponApplyForm
# from .models import Coupon

# # Create your views here.

# # @require_POST

# def apply_coupon(request):
#     now = timezone.now()
#     form = CouponApplyForm(request.POST)
#     if form.is_valid():
#         code = form.cleaned_data['code']
#         try:
#             coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
#             request.session['coupon_id'] = coupon.id
#         except Coupon.DoesNotExist:
#             request.session['coupon_id'] = None
#     return redirect(request, 'cart:cart_detail')
