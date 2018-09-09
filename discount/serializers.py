from rest_framework import serializers

from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):

	image = serializers.ImageField(max_length=None, use_url=True)
	
	class Meta:
	    model = Discount
	    fields = ('id', 'title', 'image', 'description')
