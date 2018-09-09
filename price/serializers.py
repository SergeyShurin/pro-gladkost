from rest_framework import serializers

from .models import Price

class PriceSerializer(serializers.ModelSerializer):
	
	class Meta:
	    model = Price
	    fields = ('id', 'title', 'time', 'price_man', 'price_woman')
