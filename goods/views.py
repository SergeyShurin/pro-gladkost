from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import Good
from .models import Order
from .models import OrderItem
from .serializers import OrderSerializer
from .serializers import GoodSerializer
from .serializers import OrderItemSerializer

class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all().order_by('name')
    serializer_class = GoodSerializer

class OrderViewSet(views.APIView):

	def get(self, request, format=None):
		queryset = Order.objects.all()
		serializer = OrderSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):

		order_data_list = request.data.pop('order_item')
		pk_list = []
		for order_data in order_data_list:
			order_item_serializator = OrderItemSerializer(data=order_data)
			if order_item_serializator.is_valid():
				order_item = order_item_serializator.save()
				pk_list.append(order_item.pk)
			else: return Response(order_item_serializator.errors, status=status.HTTP_400_BAD_REQUEST)

		request.data.update({'order_item': pk_list})

		order_serializator = OrderSerializer(data=request.data)

		if order_serializator.is_valid():
			order_serializator.save()
			return Response(order_serializator.data, status=status.HTTP_201_CREATED)
		else: return Response(order_serializator.errors, status=status.HTTP_400_BAD_REQUEST)