from django.shortcuts import render

# Create your views here.

from rest_framework import views
from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import Enrol
from .serializers import EnrolSerializer

class EnrolViewSet(views.APIView):
    
	def get(self, request, format=None):
		queryset = Enrol.objects.all()
		serializer = EnrolSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):

		list_procedures = request.data.pop('list')

		enrol_serializator = EnrolSerializer(data=request.data)

		if enrol_serializator.is_valid():
			enrol_serializator.save()
			return Response(enrol_serializator.data, status=status.HTTP_201_CREATED)
		else: return Response(enrol_serializator.errors, status=status.HTTP_400_BAD_REQUEST)

