from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import views
from .models import Discount
from .serializers import DiscountSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer