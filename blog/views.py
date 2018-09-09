from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import views
from .models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('title')
    serializer_class = BlogSerializer