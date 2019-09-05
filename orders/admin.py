from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity', 'order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'phone',
                    'billing_address1', 'billing_address2', 'city', 'created_at', 'updated_at', 'paid']
    list_filter = ['created_at', 'updated_at', 'paid']
    inlines = [OrderItemInline]
    # actions = [export_to_csv]


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
