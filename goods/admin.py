from django.contrib import admin


# Register your models here.

from .models import Good
from .models import Order
from .models import OrderItem

class GoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	fields = ('name', 'price', 'description', 'image')

class OrderAdmin(admin.ModelAdmin):
	fields = ('customer_name', 'customer_surname', 'phone', 'added', 'paid')
	readonly_fields = ('customer_name', 'customer_surname', 'phone', 'added')
	exclude = ('order_item',)
	list_display = ('id', 'get_full_name', 'get_products', 'phone', 'paid', 'added')

admin.site.register(Good, GoodAdmin)
admin.site.register(Order, OrderAdmin)