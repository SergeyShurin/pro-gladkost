from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import views
from .models import Price
from .serializers import PriceSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('title')
    serializer_class = PriceSerializer