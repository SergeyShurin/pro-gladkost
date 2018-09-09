from rest_framework import serializers

from .models import Good
from .models import Order
from .models import OrderItem

class GoodSerializer(serializers.ModelSerializer):

	image = serializers.ImageField(max_length=None, use_url=True)
	
	class Meta:
	    model = Good
	    fields = ('id', 'name', 'price', 'image', 'description')

class OrderItemSerializer(serializers.ModelSerializer):

	class Meta:  
	    model = OrderItem
	    fields = ('name', 'quantity',)

class OrderSerializer(serializers.ModelSerializer):

	class Meta:
	    model = Order
	    fields = ('customer_name', 'customer_surname', 'order_item', 'phone')